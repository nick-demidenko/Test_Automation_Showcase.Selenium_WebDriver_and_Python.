from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
from selenium.common.exceptions import TimeoutException
from fixtures.driver_setups import chrome_setup
from page_objects.elements_section.RadioButtonPage import RadioButtonPage


def test_radio_button_functionality():
    driver = webdriver.Chrome()
    radio_button_page = RadioButtonPage(driver)
    radio_button_page.load()
    chrome_setup.set_up_driver(driver)

    # Manage consent pop-up if it appears
    try:
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(RadioButtonPage.GIVE_DATA_USAGE_CONSENT_BTN)).click()
    except TimeoutException:
        print("Consent pop-up did not appear, or the button was not clickable.")

    # Interactions with the page
    radio_button_page.select_yes_radio()
    assert radio_button_page.is_yes_radio_selected, "The Yes radio button is not selected."

    radio_button_page.select_impressive_radio()
    assert radio_button_page.is_impressive_radio_selected, "The Impressive radio button is not selected."

    # 'No' radio button is disabled; thus, we cannot interact with it

    print("Radio button functionality test passed.")
    driver.quit()


if __name__ == "__main__":
    test_radio_button_functionality()
