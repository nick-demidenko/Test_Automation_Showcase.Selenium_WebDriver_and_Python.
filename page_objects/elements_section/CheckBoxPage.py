from selenium.webdriver.common.by import By


class CheckBoxPage:
    URL = 'https://demoqa.com/checkbox'

    # Locators
    GIVE_DATA_USAGE_CONSENT_BTN = (By.CSS_SELECTOR, ".fc-button.fc-cta-consent.fc-primary-button")

    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    COLLAPSE_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Collapse all']")
    HOME_CHECKBOX = (By.CSS_SELECTOR, "label[for='tree-node-home'] span.rct-checkbox")
    RESULT = (By.CLASS_NAME, 'display-result')
    SELECTED_ITEMS = (By.CLASS_NAME, "text-success")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    # region Functions to find actionable elements
    def find_expand_all_button(self):
        return self.driver.find_element(*self.EXPAND_ALL_BUTTON)

    def find_collapse_all_button(self):
        return self.driver.find_element(*self.COLLAPSE_ALL_BUTTON)

    def find_home_checkbox(self):
        return self.driver.find_element(*self.HOME_CHECKBOX)

    def find_result_element(self):
        return self.driver.find_element(*self.RESULT)

    def find_selected_items_text_element(self):
        return self.driver.find_elements(*self.SELECTED_ITEMS)
    # endregion

    # region Functions that performa actions
    def expand_all(self):
        self.find_expand_all_button().click()

    def collapse_all(self):
        self.find_collapse_all_button().click()

    def select_home_checkbox(self):
        self.find_home_checkbox().click()

    @property
    def get_result_text(self):
        return self.find_result_element().text

    def get_selected_items_text(self):
        selected_items = self.find_selected_items_text_element()
        return [item.text for item in selected_items]
    # endregion
