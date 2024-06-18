from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)


def get_description(href: str):
    driver.get(href)
    try:
        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "item-cataloged-data"))
        )
        children = driver.find_elements(By.CSS_SELECTOR, "#item-cataloged-data > *")
        description = dict()
        for i in range(0, len(children), 2):  
            key = children[i].text.strip()
            value = children[i + 1].text.strip()
            description[key] = value
        return description
    except Exception as e:
        print(f"Error getting description: {e}")
        return None