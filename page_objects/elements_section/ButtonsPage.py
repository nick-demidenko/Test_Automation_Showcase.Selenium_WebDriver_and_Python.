from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains


class ButtonsPage:
    URL = 'https://demoqa.com/buttons'

    # Locators
    DOUBLE_CLICK_BUTTON = (By.ID, "doubleClickBtn")
    RIGHT_CLICK_BUTTON = (By.ID, "rightClickBtn")
    CLICK_ME_BUTTON = (By.XPATH, "//button[text()='Click Me']")
    DOUBLE_CLICK_MESSAGE = (By.ID, "doubleClickMessage")
    RIGHT_CLICK_MESSAGE = (By.ID, "rightClickMessage")
    DYNAMIC_CLICK_MESSAGE = (By.ID, "dynamicClickMessage")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.action_chains = ActionChains(driver)

    def load(self):
        self.driver.get(self.URL)

    def double_click_button(self):
        button = self.driver.find_element(*self.DOUBLE_CLICK_BUTTON)
        self.action_chains.double_click(button).perform()

    def right_click_button(self):
        button = self.driver.find_element(*self.RIGHT_CLICK_BUTTON)
        self.action_chains.context_click(button).perform()

    def click_me_button(self):
        button = self.driver.find_element(*self.CLICK_ME_BUTTON)
        button.click()

    def get_double_click_message(self):
        return self.driver.find_element(*self.DOUBLE_CLICK_MESSAGE).text

    def get_right_click_message(self):
        return self.driver.find_element(*self.RIGHT_CLICK_MESSAGE).text

    def get_dynamic_click_message(self):
        return self.driver.find_element(*self.DYNAMIC_CLICK_MESSAGE).text