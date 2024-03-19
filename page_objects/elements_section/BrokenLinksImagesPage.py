from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions


class BrokenLinksImagesPage:
    URL = 'https://demoqa.com/broken'

    # region Locators
    # region Images
    VALID_IMAGE = (By.CSS_SELECTOR, 'img[src="/images/Toolsqa.jpg"')
    BROKEN_IMAGE = (By.CSS_SELECTOR, 'img[src="/images/Toolsqa_1.jpg"')

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    # region Functions that find images
    def find_and_return_valid_image(self):
        valid_image = self.driver.find_element(*self.VALID_IMAGE)
        return valid_image

    def find_and_return_broken_image(self):
        broken_image = self.driver.find_element(*self.BROKEN_IMAGE)
        return broken_image
