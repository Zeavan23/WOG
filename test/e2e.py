from selenium import webdriver
import sys
import time

def test_scores_service(app_url):
    driver = None
    try:
        driver = webdriver.Chrome()

        driver.get(app_url)
        time.sleep(5)  # Wait for the page to load

        score_element = driver.find_element_by_id("score")

        score_text = score_element.text
        score = int(score_text)
        if 1 <= score <= 1000:
            return True
        else:
            return False
    except Exception as e:
        print("An error occurred:", e)
        return False
    finally:
        if driver:
            driver.quit()

def main_function():
    app_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:5000"

    if test_scores_service(app_url):
        return 0  # Tests passed
    else:
        return -1  # Tests failed

if __name__ == "__main__":
    exit_code = main_function()
    sys.exit(exit_code)
