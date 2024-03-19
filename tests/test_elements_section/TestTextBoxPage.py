from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
from selenium.common.exceptions import TimeoutException
from fixtures import test_data
from fixtures.driver_setups import chrome_setup

from page_objects.elements_section.TextBoxPage import TextBoxPage

# region Initialize and set up the WebDriver
driver = webdriver.Chrome()
text_box_page = TextBoxPage(driver)
text_box_page.load()
chrome_setup.set_up_driver(driver)
# endregion

# region Manage consent pop-up if it appears
try:
    (WebDriverWait(driver, 10).
     until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                                     '.fc-button.fc-cta-consent.fc-primary-button'))))
    text_box_page.give_data_usage_consent()
except TimeoutException:
    print("Consent pop-up did not appear, or the button was not clickable. Test is continued.")
# endregion

# region Interact with the page
try:
    text_box_page.enter_full_name(test_data.full_name_input)
    text_box_page.enter_email(test_data.email_input)
    text_box_page.enter_current_address(test_data.current_address_input)
    text_box_page.enter_permanent_address(test_data.permanent_address_input)
    driver.execute_script("arguments[0].scrollIntoView(true);",
                          text_box_page.find_and_return_submit_inputs_btn())
    text_box_page.submit_inputs()
except AssertionError as e:
    print(f"Assertion failed: {e}. Check interactions with the page.")
# endregion

# region Check output in the input fields after input submission.
try:
    assert test_data.full_name_input in text_box_page.get_full_name_output_from_input_field
except AssertionError as e:
    print(f"Assertion failed:{e}. Check the Full Name output in the input field.")
try:
    assert test_data.email_input in text_box_page.get_email_output_from_input_field
except AssertionError as e:
    print(f"Assertion failed:{e} Check the Email output in the input field.")
try:
    assert test_data.current_address_input in text_box_page.get_current_address_output_from_input_field
except AssertionError as e:
    print(f"Assertion failed:{e} Check the Current Address output in the input field.")
try:
    assert test_data.permanent_address_input in text_box_page.get_permanent_address_output_from_input_field
except AssertionError as e:
    print(f"Assertion failed:{e} Check the Permanent Address output in the input field.")
# endregion

# region Check output in the output fields after input submission
try:
    assert test_data.full_name_input in text_box_page.get_full_name_output_from_output_field
except AssertionError as e:
    print(f"Assertion failed:{e}. Check the Full Name output in the output field.")
try:
    assert test_data.email_input in text_box_page.get_email_output_from_output_field
except AssertionError as e:
    print(f"Assertion failed:{e} Check the Email output in the output field.")
try:
    assert test_data.current_address_input in text_box_page.get_current_address_output_from_output_field
except AssertionError as e:
    print(f"Assertion failed:{e} Check the Current Address output in the output field.")
try:
    assert test_data.permanent_address_input in text_box_page.get_permanent_address_output_from_output_field
except AssertionError as e:
    print(f"Assertion failed:{e} Check the Permanent Address output in the output field.")
# endregion


try:
    print("Cleanup and Resource Management.")
finally:
    driver.quit()
