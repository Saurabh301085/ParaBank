from Parabank.Utilities.base_page import ParaBankWebElements
from selenium.webdriver.common.by import By


class ParaBankLogin(ParaBankWebElements):

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_button = (By.XPATH, "//input[@type='submit']")

    error_message = (
        By.XPATH,
        "//p[contains(text(),'The username and password could not be verified')]"
    )

    def login_details(self, name, pwd):
        self.enter_text(self.username, name)
        self.enter_text(self.password, pwd)
        self.click_button(self.login_button)

    def get_error_message(self):
        return self.get_text(self.error_message)

