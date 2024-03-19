from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from page_objects.elements_section.WebTablesPage import WebTablesPage


def test_add_new_record_to_web_table():
    driver = webdriver.Chrome()
    driver.maximize_window()
    web_tables_page = WebTablesPage(driver)
    web_tables_page.load()

    # Consent popup handling
    try:
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(WebTablesPage.GIVE_DATA_USAGE_CONSENT_BTN)
        ).click()
        print("Clicked the consent popup.")
    except TimeoutException:
        print("Consent pop-up did not appear, or the button was not clickable. Test is continued.")

    initial_entries_text = web_tables_page.get_all_entries_text()
    print(f"Initial entries: {initial_entries_text}")

    # Add a new record
    web_tables_page.click_add_button()
    web_tables_page.submit_new_record("John", "Doe", "johndoe@example.com",
                                      "30", "10000", "IT")

    # Wait for text to appear in the table or for the table to update
    new_entry_text = "John Doe"
    web_tables_page.wait_for_text_to_be_present_in_table(new_entry_text)

    all_entries_after_addition = web_tables_page.get_all_entries_text()
    print(f"All entries after addition: {all_entries_after_addition}")

    # Verify new record was added successfully
    assert new_entry_text in " ".join(all_entries_after_addition), "New entry text is not visible in the table."

    print("Test passed: New record added successfully.")
    driver.quit()


if __name__ == "__main__":
    test_add_new_record_to_web_table()
