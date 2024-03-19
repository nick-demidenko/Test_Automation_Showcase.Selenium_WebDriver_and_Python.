from selenium.webdriver.common.by import By


class TextBoxPage:
    URL = 'https://demoqa.com/text-box'

    # region Locators

    GIVE_DATA_USAGE_CONSENT_BTN = (By.CSS_SELECTOR, ".fc-button.fc-cta-consent.fc-primary-button")

    # region Input fields
    FULL_NAME_INPUT_FIELD = (By.ID, 'userName')
    EMAIL_INPUT_FIELD = (By.ID, 'userEmail')
    CURRENT_ADDRESS_INPUT_FIELD = (By.ID, 'currentAddress')
    PERMANENT_ADDRESS_INPUT_FIELD = (By.ID, 'permanentAddress')
    # endregion

    # region Buttons
    SUBMIT_BUTTON = (By.ID, 'submit')
    # endregion

    # region Fields
    FULL_NAME_OUTPUT_FIELD = (By.ID, 'name')
    EMAIL_OUTPUT_FIELD = (By.ID, 'email')
    CURRENT_ADDRESS_OUTPUT_FIELD = (By.CSS_SELECTOR, "#currentAddress.mb-1")
    PERMANENT_ADDRESS_OUTPUT_FIELD = (By.CSS_SELECTOR, "#permanentAddress.mb-1")
    # endregion
    # endregion

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def find_and_return_give_consent_btn(self):
        give_consent_btn = self.driver.find_element(*self.GIVE_DATA_USAGE_CONSENT_BTN)
        return give_consent_btn

    # region Functions that find elements to which the input will be provided
    def find_and_return_full_name_input_field(self):
        full_name_input_field = self.driver.find_element(*self.FULL_NAME_INPUT_FIELD)
        return full_name_input_field

    def find_and_return_email_input_field(self):
        email_input_field = self.driver.find_element(*self.EMAIL_INPUT_FIELD)
        return email_input_field

    def find_and_return_current_address_input_field(self):
        current_address_input_field = self.driver.find_element(*self.CURRENT_ADDRESS_INPUT_FIELD)
        return current_address_input_field

    def find_and_return_permanent_address_input_field(self):
        permanent_address_input_field = self.driver.find_element(*self.PERMANENT_ADDRESS_INPUT_FIELD)
        return permanent_address_input_field

    def find_and_return_submit_inputs_btn(self):
        submit_inputs_btn = self.driver.find_element(*self.SUBMIT_BUTTON)
        return submit_inputs_btn

    # region Functions that provide input to the input fields

    def give_data_usage_consent(self):
        give_consent_btn = self.find_and_return_give_consent_btn()
        give_consent_btn.click()

    def enter_full_name(self, name):
        full_name_input_field = self.find_and_return_full_name_input_field()
        full_name_input_field.clear()
        full_name_input_field.send_keys(name)

    def enter_email(self, email):
        email_input_field = self.find_and_return_email_input_field()
        email_input_field.clear()
        email_input_field.send_keys(email)

    def enter_current_address(self, email):
        email_field = self.find_and_return_current_address_input_field()
        email_field.clear()
        email_field.send_keys(email)

    def enter_permanent_address(self, email):
        email_field = self.find_and_return_permanent_address_input_field()
        email_field.clear()
        email_field.send_keys(email)

    def submit_inputs(self):
        self.find_and_return_submit_inputs_btn().click()

    # endregion

    # region Functions that find and return output from the input fields
    @property
    def get_full_name_output_from_input_field(self):
        return self.find_and_return_full_name_input_field().get_attribute("value")

    @property
    def get_email_output_from_input_field(self) -> object:
        return self.find_and_return_email_input_field().get_attribute("value")

    @property
    def get_current_address_output_from_input_field(self) -> object:
        return self.find_and_return_current_address_input_field().get_attribute("value")

    @property
    def get_permanent_address_output_from_input_field(self) -> object:
        return self.find_and_return_permanent_address_input_field().get_attribute("value")
    # endregion

    # region Functions that find and return elements where output will appear
    def find_and_return_full_name_output_field(self):
        full_name_output_field = self.driver.find_element(*self.FULL_NAME_OUTPUT_FIELD)
        return full_name_output_field

    def find_and_return_email_output_field(self):
        email_output_field = self.driver.find_element(*self.EMAIL_OUTPUT_FIELD)
        return email_output_field

    def find_and_return_current_address_output_field(self):
        current_address_output_field = self.driver.find_element(*self.CURRENT_ADDRESS_OUTPUT_FIELD)
        return current_address_output_field

    def find_and_return_permanent_address_output_field(self):
        permanent_address_output_field = self.driver.find_element(*self.PERMANENT_ADDRESS_OUTPUT_FIELD)
        return permanent_address_output_field

    # region Functions that return output from the output field
    @property
    def get_full_name_output_from_output_field(self):
        return self.find_and_return_full_name_output_field().text

    @property
    def get_email_output_from_output_field(self) -> object:
        return self.find_and_return_email_output_field().text

    @property
    def get_current_address_output_from_output_field(self) -> object:
        return self.find_and_return_current_address_output_field().text

    @property
    def get_permanent_address_output_from_output_field(self) -> object:
        return self.find_and_return_permanent_address_output_field().text
    # endregion
