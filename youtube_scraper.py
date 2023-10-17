from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import csv
import time

# Ruta del geckodriver de Firefox
firefox_driver_path = "C:\\FirefoxDriver\\geckodriver.exe"
webdriver_service = Service(firefox_driver_path)

# Creamos las opciones para Firefox
firefox_options = webdriver.FirefoxOptions()
firefox_options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"  # Asegúrate que esta ruta es correcta

# Iniciamos el driver de Firefox
driver = webdriver.Firefox(service=webdriver_service, options=firefox_options)

# URL del video de YouTube
url = 'https://www.youtube.com/watch?v=weKocqMyF1I'

try:
    driver.get(url)
    time.sleep(5)
    old_comments_count = 0
    same_count = 0

    with open('youtube_comments.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Author", "Comment"])

        id_counter = 1

        while True:
            ActionChains(driver).key_down(Keys.PAGE_DOWN).perform()
            time.sleep(1)

            comments_elements = driver.find_elements(By.CSS_SELECTOR, "#content-text")
            author_elements = driver.find_elements(By.CSS_SELECTOR, "#author-text span")

            if len(comments_elements) == old_comments_count:
                same_count += 1
            else:
                same_count = 0

            if same_count > 5 or len(comments_elements) >= 2000: 
                break

            old_comments_count = len(comments_elements)

            for comment_element, author_element in zip(comments_elements, author_elements):
                try:
                    comment_text = comment_element.text.replace('\n', ' ')
                    author_text = author_element.text
                    writer.writerow([id_counter, author_text, comment_text])
                    id_counter += 1
                except NoSuchElementException:
                    pass

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    driver.quit()