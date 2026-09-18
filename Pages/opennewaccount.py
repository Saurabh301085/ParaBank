from Parabank.Utilities.base_page import ParaBankWebElements
from selenium.webdriver.common.by import By


class NewAccount(ParaBankWebElements):
    new_account = (By.XPATH, "//a[normalize-space()='Open New Account']")
    acc_type = (By.XPATH, "//select[@id='type']")
    existing_acc = (By.ID, "fromAccountId")
    open_new_acc_button = (By.XPATH, "//input[@value='Open New Account']")
    acc_open_message = (By.XPATH,"//p[normalize-space()='Congratulations, your account is now open.']")
    def open_new_acc(self):
        self.click_button(self.new_account)

    def select_account_type(self, value):
        self.select_dropdown(self.acc_type, value)

    def existing_account(self, ex_acc):
        self.select_dropdown(self.existing_acc, ex_acc)

    def click_open_new_acc_button(self):
        self.click_button(self.open_new_acc_button)

    def success_msg(self):
       return self.get_text(self.acc_open_message)