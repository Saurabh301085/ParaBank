from Parabank.Utilities.base_page import ParaBankWebElements
from selenium.webdriver.common.by import By
from Parabank.Utilities.logger import get_logger


class request_loan(ParaBankWebElements):

    logger = get_logger()

    r_loan = (By.XPATH, "//a[normalize-space()='Request Loan']")
    loan_amount = (By.ID, "amount")
    down_payment = (By.ID, "downPayment")
    from_account = (By.ID, "fromAccountId")
    apply = (By.XPATH, "//input[@value='Apply Now']")
    insufficient_funds_msg = (
        By.XPATH,
        "//p[contains(text(),'You do not have sufficient funds')]"
    )
    sufficient_fund_msg = (
        By.XPATH, "//p[normalize-space()='Congratulations, your loan has been approved.']"
    )

    def request_loan_link(self):
        self.logger.info("Click the request link to open")
        self.click_button(self.r_loan)

    def request_loan_amount(self, amount, d_payment, acc_value):
        self.logger.info("Enter the loan amount u wanna apply for")
        self.enter_text(self.loan_amount, amount)

        self.logger.info("Enter down payment amount")
        self.enter_text(self.down_payment, d_payment)

        self.logger.info("select existin account number")
        self.select_dropdown(self.from_account, acc_value)

        self.logger.info("Press Loan button")
        self.click_button(self.apply)

    def get_insufficient_funds_message(self):
        self.logger.warning("insufficient_funds")
        return self.get_text(self.insufficient_funds_msg)

    def get_sufficient_funds_message(self):
        self.logger.info("Success!")
        return self.get_text(self.sufficient_fund_msg)
