from selenium import webdriver

def test_scores_service(app_url):
    driver = None
    try:
        driver = webdriver.Chrome()

        driver.get(app_url)

        driver.implicitly_wait(10)

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
        return 0  # Tests passés
    else:
        return -1  # Tests échoués

if __name__ == "__main__":
    import sys
    exit_code = main_function()
    exit(exit_code)
