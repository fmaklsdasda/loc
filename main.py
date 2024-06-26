import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import urllib.request

from selenium.common.exceptions import TimeoutException

from page_parser import PageParser


driver = webdriver.Chrome()
driver.implicitly_wait(5)

URL = "https://www.loc.gov/collections/world-digital-library/"


def get_list():
    i = 1
    list = []
    while True:
        driver.get(f"{URL}/?q=Tsybikov&sp={i}")
        i += 1
        try:
            element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.ID, "results"))
            )
            if not element:
                raise Exception("Results not founded")
            else:
                items = driver.find_elements(By.CLASS_NAME, "item")
                for item in items:
                    title_element = item.find_element(By.CSS_SELECTOR, ".item-description-title a")
                    title_link = title_element.get_attribute("href")
                    list.append(title_link)
        except TimeoutException as er:
            print(er)
            break
        except Exception as er:
            print(er)
            break
    return list



def get_page_info():

    html_source = driver.page_source
    return html_source


def main():
    # list_items = get_list() 
    list_items = [2021670601]
    page_descriptions = []
    for id in list(list_items):
        parser = PageParser(id = id)
        parser.get_description()
        parser.get_photo_url()
        page_descriptions.append(parser.description)
        if parser.photo_url:
            urllib.request.urlretrieve(parser.photo_url, f"{parser.id}.jpg")
    
    keys = page_descriptions[0].keys()

    with open('description.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(page_descriptions)
 
if __name__ == "__main__":
    main()
