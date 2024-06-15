from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Переход на сайт
url = "https://www.loc.gov/item/2021670601/"
driver.get(url)

title_element = driver.find_element(By.XPATH, "//div[@id='item-title']/h1")
description_elements = driver.find_elements(By.XPATH, "//div[@class='item-summary']/p")

title = title_element.text
descriptions = [element.text for element in description_elements]

print("Title:", title)
for i, description in enumerate(descriptions, start=1):
    print(f"Description {i}: {description}")

driver.quit()