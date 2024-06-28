from selenium import webdriver
import time

def test_scores_service(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)  # Let the user actually see something!
    score_element = driver.find_element_by_id("score")
    score = int(score_element.text)
    driver.quit()
    return 1 <= score <= 1000

def main_function():
    url = "http://localhost:8777/scores/lior"
    if test_scores_service(url):
        print("Test passed")
        exit(0)
    else:
        print("Test failed")
        exit(-1)

if __name__ == "__main__":
    main_function()
