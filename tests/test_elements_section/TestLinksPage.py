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
from page_objects.elements_section.LinksPage import LinksPage


class TestLinksPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.links_page = LinksPage(self.driver)
        self.links_page.load()
        chrome_setup.set_up_driver(self.driver)
        give_data_usage_consent(self.driver)

    # region Testing links that open in another tab
    def test_static_home_link(self):
        original_tab = self.driver.current_window_handle

        home_link = self.links_page.find_and_return_home_link()
        home_link.click()

        all_tabs = self.driver.window_handles
        new_tab = [tab for tab in all_tabs if tab != original_tab][0]
        self.driver.switch_to.window(new_tab)

        WebDriverWait(self.driver, 10)

        try:
            assert self.driver.current_url == test_data.home_static_url
            self.driver.close()
            self.driver.switch_to.window(original_tab)
        except AssertionError as e:
            print(f"Assertion failed:{e}. Check static home btn.")

    def test_dynamic_home_link(self):
        original_tab = self.driver.current_window_handle

        home_link = self.links_page.find_and_return_dynamic_home_link()
        home_link.click()

        all_tabs = self.driver.window_handles
        new_tab = [tab for tab in all_tabs if tab != original_tab][0]
        self.driver.switch_to.window(new_tab)

        time.sleep(10)

        try:
            assert self.driver.current_url == test_data.home_dynamic_url
            self.driver.close()
            self.driver.switch_to.window(original_tab)
        except AssertionError as e:
            print(f"Assertion failed:{e}. Check static home btn.")

    # endregion

    # region Testing links that make API calls
    def test_create_link(self):
        created_link = self.links_page.find_and_return_created_link()

        try:
            created_link.click()
            time.sleep(5)
            assert (test_data.created_link_output_text ==
                    self.links_page.return_response_text_field_output())
        except AssertionError as e:
            print(f"Assertion failed:{e}. Check 'CREATED' link.")

    def test_no_content_link(self):
        no_content_link = self.links_page.find_and_return_no_content_link()

        try:
            no_content_link.click()
            time.sleep(5)
            assert (test_data.no_content_link_output_text ==
                    self.links_page.return_response_text_field_output())
        except AssertionError as e:
            print(f"Assertion failed:{e}. Check 'NO_CONTENT' link.")

    def test_no_moved_link(self):
        moved_link = self.links_page.find_and_return_moved_link()

        try:
            moved_link.click()
            time.sleep(5)
            assert (test_data.moved_link_output_text ==
                    self.links_page.return_response_text_field_output())
        except AssertionError as e:
            print(f"Assertion failed:{e}. Check 'MOVED' link.")

    def test_bad_request_link(self):
        bad_request_link = self.links_page.find_and_return_bad_request_link()

        try:
            bad_request_link.click()
            time.sleep(5)
            assert (test_data.bad_request_output_text ==
                    self.links_page.return_response_text_field_output())
        except AssertionError as e:
            print(f"Assertion failed:{e}. Check 'BAD_REQUEST' link.")

    def test_unauthorized_link(self):
        unauthorized_link = self.links_page.find_and_return_unauthorized_link()

        try:
            unauthorized_link.click()
            time.sleep(5)
            assert (test_data.unauthorized_link_output_text ==
                    self.links_page.return_response_text_field_output())
        except AssertionError as e:
            print(f"Assertion failed:{e}. Check 'UNAUTHORIZED' link.")

    def test_forbidden_link(self):
        forbidden_link = self.links_page.find_and_return_forbidden_link()

        try:
            forbidden_link.click()
            time.sleep(5)
            assert (test_data.forbidden_link_output_text ==
                    self.links_page.return_response_text_field_output())
        except AssertionError as e:
            print(f"Assertion failed:{e}. Check 'FORBIDDEN' link.")

    def test_not_found_link(self):
        not_found_link = self.links_page.find_and_return_not_found_link()
        util.bring_element_into_view(self.driver, not_found_link)
        time.sleep(5)
        not_found_link.click()
        try:

            time.sleep(5)
            assert (test_data.not_found_link_output_text ==
                    self.links_page.return_response_text_field_output())
        except AssertionError as e:
            print(f"Assertion failed:{e}. Check 'NOT_FOUND' link.")

    # endregion

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
