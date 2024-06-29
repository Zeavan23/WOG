from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_scores_service(app_url):
    chrome_options = Options()
    chrome_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(executable_path=chrome_service.path, options=chrome_options)

    try:
        driver.get(app_url)

        # Attendre jusqu'à 60 secondes que l'élément soit visible
        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/h1'))
        )

        # Récupérer le texte de l'élément score
        score_element = driver.find_element(By.XPATH, '/html/body/h1')
        score_value = int(score_element.text.split()[-1])

        # Affichage du score pour débogage
        print(f"Score obtenu : {score_value}")

        # Vérifier si le score est entre 1 et 1000
        if 1 <= score_value <= 1000:
            return True
        else:
            return False

    except Exception as e:
        print(f"Exception lors de la recherche de l'élément : {e}")
        return False

    finally:
        driver.quit()

def main_function():
    app_url = 'http://localhost:8777/scores/lior'  # Remplacez par l'URL correcte de votre application
    if test_scores_service(app_url):
        return 0  # Tests réussis
    else:
        return -1  # Tests échoués

if __name__ == "__main__":
    exit_code = main_function()
    exit(exit_code)
