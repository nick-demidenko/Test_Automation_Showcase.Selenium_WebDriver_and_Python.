from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RadioButtonPage:
    URL = 'https://demoqa.com/radio-button'

    # Locators
    GIVE_DATA_USAGE_CONSENT_BTN = (By.CSS_SELECTOR, ".fc-button.fc-cta-consent.fc-primary-button")
    YES_RADIO_BTN = (By.XPATH, "//label[@for='yesRadio']")
    IMPRESSIVE_RADIO_BTN = (By.XPATH, "//label[@for='impressiveRadio']")
    NO_RADIO_BTN = (By.XPATH, "//label[@for='noRadio']")
    SELECTED_MESSAGE = (By.CLASS_NAME, 'mt-3')

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    # Methods that find elements
    def find_consent_button(self):
        return self.driver.find_element(*self.GIVE_DATA_USAGE_CONSENT_BTN)

    def find_yes_radio_button(self):
        return self.driver.find_element(*self.YES_RADIO_BTN)

    def find_impressive_radio_button(self):
        return self.driver.find_element(*self.IMPRESSIVE_RADIO_BTN)

    def find_no_radio_button(self):
        return self.driver.find_element(*self.NO_RADIO_BTN)

    def find_selected_message_element(self):
        return self.driver.find_element(*self.SELECTED_MESSAGE)

    # Methods that perform actions
    def give_data_usage_consent(self):
        self.find_consent_button().click()

    def select_yes_radio(self):
        self.find_yes_radio_button().click()

    def select_impressive_radio(self):
        self.find_impressive_radio_button().click()

    # 'No' radio button is generally disabled and not meant for interaction in this context.
    # If needed, a similar method can be defined for it.

    @property
    def is_yes_radio_selected(self):
        return 'Yes' in self.find_selected_message_element().text

    @property
    def is_impressive_radio_selected(self):
        return 'Impressive' in self.find_selected_message_element().text
