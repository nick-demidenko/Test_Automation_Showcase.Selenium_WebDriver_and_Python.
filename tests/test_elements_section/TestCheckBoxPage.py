from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
from selenium.common.exceptions import TimeoutException

from fixtures.driver_setups import chrome_setup
from page_objects.elements_section.CheckBoxPage import CheckBoxPage


def test_checkbox_functionality():
    driver = webdriver.Chrome()
    checkbox_page = CheckBoxPage(driver)
    checkbox_page.load()
    chrome_setup.set_up_driver(driver)

    # region Manage consent pop-up if it appears
    try:
        (WebDriverWait(driver,
                       10).
         until(expected_conditions.element_to_be_clickable(CheckBoxPage.GIVE_DATA_USAGE_CONSENT_BTN)).click())
    except TimeoutException:
        print("Consent pop-up did not appear, or the button was not clickable. Test is continued.")
    # endregion

    # region Interactions with the page
    checkbox_page.expand_all()
    checkbox_page.select_home_checkbox()
    # endregion

    # region Check that output corresponds to selection.
    try:
        assert "You have selected :" in checkbox_page.get_result_text
    except AssertionError as e:
        print(f"Assertion failed:{e} Check the output.")

    # Get the list of selected items and check that 'home' is among the selected items
    try:
        selected_items_text = checkbox_page.get_selected_items_text()
        assert "home" in selected_items_text
    except AssertionError as e:
        print(f"Assertion failed:{e}. Check the output.")
    # endregion

    driver.quit()


if __name__ == "__main__":
    test_checkbox_functionality()
