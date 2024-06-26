from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageParser:
    url = "https://www.loc.gov/item"

    def __init__(self, id: int) -> None:
        self.id = id
        href = f"{self.url}/{self.id}"
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get(href)
        self.driver = driver
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "item-cataloged-data"))
        )

    def get_description(self):

        try:
            children = self.driver.find_elements(
                By.CSS_SELECTOR, "#item-cataloged-data > *"
            )
            description = dict()
            for i in range(0, len(children), 2):
                key = children[i].text.strip()

                value_elem = children[i + 1]
                value_items = value_elem.find_elements(By.CSS_SELECTOR, "li")
                value = [
                    li_elem.text.strip().replace("-  ", "") for li_elem in value_items
                ]
                description[key] = value
            return description
        except Exception as e:
            print(f"Error getting description: {e}")
            return None


if __name__ == "__main__":
    
    parser = PageParser(id=2021670601)
    print(parser.get_description())
