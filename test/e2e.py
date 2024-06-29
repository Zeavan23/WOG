import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_scores_service(app_url):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    try:
        driver.get(app_url)

        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/h1'))
        )

        score_element = driver.find_element(By.XPATH, '/html/body/h1')
        score_text = score_element.text

        # Utiliser une expression régulière pour extraire le nombre
        match = re.search(r'\d+', score_text)
        if match:
            score_value = int(match.group())
            print(f"Score obtenu : {score_value}")

            return 1 <= score_value <= 1000
        else:
            print("Aucun score trouvé dans le texte.")
            return False

    except Exception as e:
        print(f"Exception lors de la recherche de l'élément : {e}")
        return False

    finally:
        driver.quit()

def main_function():
    app_url = 'http://localhost:8777/scores/lior'
    if test_scores_service(app_url):
        print("Test réussi : Le score est dans la plage correcte.")
        return 0
    else:
        print("Test échoué : Le score n'est pas dans la plage attendue ou l'élément n'est pas trouvé.")
        return -1

if __name__ == "__main__":
    exit_code = main_function()
    exit(exit_code)
