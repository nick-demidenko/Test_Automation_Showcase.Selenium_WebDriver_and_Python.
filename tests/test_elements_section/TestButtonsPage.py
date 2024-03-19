import unittest
from selenium import webdriver
from page_objects.elements_section.ButtonsPage import ButtonsPage


class TestButtonsFunctionality(unittest.TestCase):
    def setUp(self):
        # Setup code here. Adjust the WebDriver instantiation based on your browser.
        self.driver = webdriver.Chrome()
        self.buttons_page = ButtonsPage(self.driver)
        self.buttons_page.load()

    def test_button_clicks(self):
        self.buttons_page.double_click_button()
        self.assertEqual(self.buttons_page.get_double_click_message(), "You have done a double click")

        self.buttons_page.right_click_button()
        self.assertEqual(self.buttons_page.get_right_click_message(), "You have done a right click")

        self.buttons_page.click_me_button()
        self.assertEqual(self.buttons_page.get_dynamic_click_message(), "You have done a dynamic click")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
