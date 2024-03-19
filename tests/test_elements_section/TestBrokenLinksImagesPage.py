import time
import unittest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities.util import give_data_usage_consent
from fixtures import test_data
from utilities import util

from fixtures.driver_setups import chrome_setup
from page_objects.elements_section.BrokenLinksImagesPage import BrokenLinksImagesPage


class TestBrokenLinksImagesPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.broken_links_images_page = BrokenLinksImagesPage(self.driver)
        self.broken_links_images_page.load()
        chrome_setup.set_up_driver(self.driver)
        give_data_usage_consent(self.driver)

    def test_valid_image(self):
        valid_image = self.broken_links_images_page.find_and_return_valid_image()
        try:
            assert valid_image.get_attribute('naturalWidth') > 0
        except AssertionError as e:
            print(f"Assertion failed:{e}. Check 'valid' image.")

    def test_broken_image(self):
        valid_broken = self.broken_links_images_page.find_and_return_broken_image()
        try:
            assert valid_broken.get_attribute('naturalWidth') > 0
        except AssertionError as e:
            print(f"Assertion failed:{e}. Check 'broken' image.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
