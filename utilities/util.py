from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
from selenium import webdriver

# region Locators
GIVE_DATA_USAGE_CONSENT_BTN_LOCATOR = (By.CSS_SELECTOR, ".fc-button.fc-cta-consent.fc-primary-button")
# endregion


# region Methods that find elements with the help of Locators
def find_and_return_give_data_usage_consent_btn():
    give_data_usage_consent_btn = GIVE_DATA_USAGE_CONSENT_BTN_LOCATOR
    return give_data_usage_consent_btn
# endregion


# region Methods that interact with pages
def give_data_usage_consent(driver):
    try:
        (WebDriverWait(driver, 10).
         until(
            expected_conditions.
            element_to_be_clickable(
                find_and_return_give_data_usage_consent_btn())).
         click())
    except TimeoutException:
        print("Consent pop-up not available.")


def bring_element_into_view(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
# endregion
