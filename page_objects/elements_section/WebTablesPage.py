from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions

class WebTablesPage:
    URL = 'https://demoqa.com/webtables'
    GIVE_DATA_USAGE_CONSENT_BTN = (By.CSS_SELECTOR, ".fc-button.fc-cta-consent.fc-primary-button")
    ADD_BUTTON = (By.ID, 'addNewRecordButton')
    FIRST_NAME_FIELD = (By.ID, 'firstName')
    LAST_NAME_FIELD = (By.ID, 'lastName')
    EMAIL_FIELD = (By.ID, 'userEmail')
    AGE_FIELD = (By.ID, 'age')
    SALARY_FIELD = (By.ID, 'salary')
    DEPARTMENT_FIELD = (By.ID, 'department')
    SUBMIT_BUTTON = (By.ID, 'submit')
    TABLE_ROWS = (By.CSS_SELECTOR, ".rt-tbody .rt-tr-group")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    # Action methods
    def click_add_button(self):
        self.find_add_button().click()

    def submit_new_record(self, first_name, last_name, email, age, salary, department):
        self.find_first_name_field().send_keys(first_name)
        self.find_last_name_field().send_keys(last_name)
        self.find_email_field().send_keys(email)
        self.find_age_field().send_keys(age)
        self.find_salary_field().send_keys(salary)
        self.find_department_field().send_keys(department)
        self.find_submit_button().click()

    # Element find methods
    def find_add_button(self):
        return self.driver.find_element(*self.ADD_BUTTON)

    def find_first_name_field(self):
        return self.driver.find_element(*self.FIRST_NAME_FIELD)

    def find_last_name_field(self):
        return self.driver.find_element(*self.LAST_NAME_FIELD)

    def find_email_field(self):
        return self.driver.find_element(*self.EMAIL_FIELD)

    def find_age_field(self):
        return self.driver.find_element(*self.AGE_FIELD)

    def find_salary_field(self):
        return self.driver.find_element(*self.SALARY_FIELD)

    def find_department_field(self):
        return self.driver.find_element(*self.DEPARTMENT_FIELD)

    def find_submit_button(self):
        return self.driver.find_element(*self.SUBMIT_BUTTON)

    def find_table_rows(self):
        return self.driver.find_elements(*self.TABLE_ROWS)

    def get_all_entries_text(self):
        # Fetches all row elements
        rows = self.find_table_rows()
        # Retrieves text from each cell in each row and joins them with a space for easier comparison
        entries_text = [' '.join(row.text.split('\n')) for row in rows]
        return entries_text

    def wait_for_text_to_be_present_in_table(self, expected_text):
        WebDriverWait(self.driver, 10).until(
            lambda _driver: any(expected_text in entry for entry in self.get_all_entries_text()),
            message=f"Failed to find the text '{expected_text}' in the table within the timeout period."
        )