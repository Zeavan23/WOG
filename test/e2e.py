import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_scores_service(app_url):
    # Use ChromeDriverManager to get the executable path for ChromeDriver
    chrome_driver_path = ChromeDriverManager().install()

    # Set up Chrome options
    options = webdriver.ChromeOptions()

    # Initialize the Chrome WebDriver with the Service object
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(app_url)

        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/h1'))
        )

        score_element = driver.find_element(By.XPATH, '/html/body/h1')
        score_text = score_element.text

        # Use a regular expression to extract the number
        match = re.search(r'\d+', score_text)
        if match:
            score_value = int(match.group())
            print(f"Score obtained: {score_value}")

            return 1 <= score_value <= 1000
        else:
            print("No score found in the text.")
            return False

    except Exception as e:
        print(f"Exception while searching for the element: {e}")
        return False

    finally:
        driver.quit()

def main_function():
    app_url = 'http://localhost:8777/scores/lior'
    if test_scores_service(app_url):
        print("Test passed: The score is within the correct range.")
        return 0
    else:
        print("Test failed: The score is not within the expected range or the element is not found.")
        return -1

if __name__ == "__main__":
    exit_code = main_function()
    exit(exit_code)
