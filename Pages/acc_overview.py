from Parabank.Utilities.base_page import ParaBankWebElements
from selenium.webdriver.common.by import By


class Account_overview(ParaBankWebElements):
    overview_link = (By.XPATH, "//a[normalize-space()='Accounts Overview']")
    account_no = (By.XPATH, "//a[normalize-space()='13344']")

    def check_acc_overview(self):
        self.click_button(self.overview_link)
        self.click_button(self.account_no)
