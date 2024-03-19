from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions


class LinksPage:
    URL = 'https://demoqa.com/links'

    # region Locators

    # GIVE_DATA_USAGE_CONSENT_BTN = (By.CSS_SELECTOR, ".fc-button.fc-cta-consent.fc-primary-button")

    # region Locators of links that open in another tab
    HOME_LINK = (By.ID, "simpleLink")
    HOMEOPHEK_LINK = (By.ID, "dynamicLink")
    # endregion

    # region Locators of links that send API calls
    CREATED_LINK = (By.ID, "created")
    NO_CONTENT_LINK = (By.ID, "no-content")
    MOVED_LINK = (By.ID, "moved")
    BAD_REQUEST_LINK = (By.ID, "bad-request")
    UNAUTHORIZED_LINK = (By.ID, "unauthorized")
    FORBIDDEN_LINK = (By.ID, "forbidden")
    NOT_FOUND_LINK = (By.ID, "invalid-url")
    # endregion

    # region Locators of response text field
    LINK_RESPONSE_TEXT_FIELD = (By.ID, "linkResponse")

    # endregion
    # endregion

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    # region Functions that find links that open in another tab
    def find_and_return_home_link(self):
        home_link = self.driver.find_element(*self.HOME_LINK)
        return home_link

    def find_and_return_dynamic_home_link(self):
        dynamic_home_link = self.driver.find_element(*self.HOMEOPHEK_LINK)
        return dynamic_home_link

    # endregion

    # region Functions that find links that send API calls
    def find_and_return_created_link(self):
        created_link = self.driver.find_element(*self.CREATED_LINK)
        return created_link

    def find_and_return_no_content_link(self):
        no_content_link = self.driver.find_element(*self.NO_CONTENT_LINK)
        return no_content_link

    def find_and_return_moved_link(self):
        moved_link = self.driver.find_element(*self.MOVED_LINK)
        return moved_link

    def find_and_return_bad_request_link(self):
        bad_request_link = self.driver.find_element(*self.BAD_REQUEST_LINK)
        return bad_request_link

    def find_and_return_unauthorized_link(self):
        unauthorized_link = self.driver.find_element(*self.UNAUTHORIZED_LINK)
        return unauthorized_link

    def find_and_return_forbidden_link(self):
        forbidden_link = self.driver.find_element(*self.FORBIDDEN_LINK)
        return forbidden_link

    def find_and_return_not_found_link(self):
        not_found_link = self.driver.find_element(*self.NOT_FOUND_LINK)
        return not_found_link

    # endregion

    # region Functions that find elements that should display output
    def find_and_return_link_response_text_field(self):
        link_response_text_field = self.driver.find_element(*self.LINK_RESPONSE_TEXT_FIELD)
        return link_response_text_field

    # endregion

    # region Functions that extract data from elements
    def return_response_text_field_output(self):
        return self.find_and_return_link_response_text_field().text
    # endregion
