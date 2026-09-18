import time
from Parabank.Utilities.logger import get_logger
from Parabank.Pages.opennewaccount import NewAccount
from Parabank.Pages.para_login import ParaBankLogin
from Parabank.Pages.acc_overview import Account_overview
from Parabank.Pages.loan import request_loan
from Parabank.Pages.bill_pay import ParaBankPayBill
from Parabank.Pages.update_profile import ProfileUpdate


class TestLoginDtls():
    logger = get_logger()

    #
    #     # def test_login(self, driver):
    #     #     parabank = ParaBankLogin(driver)
    #     #
    #     #     # Valid Login
    #     #     parabank.login_details("john", "demo")
    #     #
    #     #     # Open New Account after successful login
    #     #     #
    #     #
    #     #     # def test_invalid_login(self,driver):
    #     #     #     pbank = ParaBankLogin(driver)
    #     #     #     time.sleep(4)
    #     #     #     pbank.login_details("saurabh", "kuril")
    #     #     #     actual_message = pbank.get_error_message()
    #     #     #     expected_message = "The username and password could not be verified."
    #     #     #
    #     #     #     assert actual_message == expected_message, (
    #     #     #         f"Expected '{expected_message}' but got '{actual_message}'"
    #     #     #     )
    #     #
    #     #     loans = request_loan(driver)
    #     #     loans.request_loan_link()
    #     #     time.sleep(2)
    #     #     loans.request_loan_amount("20", "5", "13011")
    #     #
    #     #     expected_msg = "Congratulations, your loan has been approved."
    #     #
    #     #     actual_msg = loans.get_sufficient_funds_message()
    #     #
    #     #     assert expected_msg == actual_msg
    #     #     print("Loan successfully approved")
    #     #     #     , (
    #     #     #     f"Expected '{expected_msg}' but got '{actual_msg}'"
    #     #     # )
    #     #
    #     # def test_loan_amount(self, driver):
    #     #     parabanks = ParaBankLogin(driver)
    #     #
    #     #     # Valid Login
    #     #     parabanks.login_details("john", "demo")
    #     #
    #     #     # Open New Account after successful login
    #     #     #
    #     #
    #     #     # def test_invalid_login(self,driver):
    #     #     #     pbank = ParaBankLogin(driver)
    #     #     #     time.sleep(4)
    #     #     #     pbank.login_details("saurabh", "kuril")
    #     #     #     actual_message = pbank.get_error_message()
    #     #     #     expected_message = "The username and password could not be verified."
    #     #     #
    #     #     #     assert actual_message == expected_message, (
    #     #     #         f"Expected '{expected_message}' but got '{actual_message}'"
    #     #     #     )
    #     #
    #     #     loan = request_loan(driver)
    #     #     loan.request_loan_link()
    #     #     time.sleep(2)
    #     #     loan.request_loan_amount("2000", "500", "13011")
    #     #
    #     #     actual_msg = loan.get_insufficient_funds_message()
    #     #     expected_msg = "You do not have sufficient funds for the given down payment."
    #     #
    #     #     assert actual_msg == expected_msg
    #     #     print("Loan request unsuccessful due to insufficient funds")
    #     #     #     ,(
    #     #     # f"Expected '{expected_msg}' but got '{actual_msg}'"
    #     #     # )
    #
    #     # def test_payee_bill(self, driver):
    #     #     parabank = ParaBankLogin(driver)
    #     #
    #     #     # Valid Login
    #     #     parabank.login_details("john", "demo")
    #     #
    #     #     payee = ParaBankPayBill(driver)
    #     #     self.logger.info("entered all the details required")
    #     #     payee.click_bill_pay_link()
    #     #     payee.bill_payment_form("saurabh", "39, shree ji vihar", "udaipur", "Rajasthan", "313001",
    #     #                             "283923922", "13677", "13677", "7", "350")
    #     #     time.sleep(2)
    #     #     self.logger.info("send payment done!")
    #     #     payee.send_payment()
    #
    def test_profile_update(self, driver):
        parabank = ParaBankLogin(driver)
        #
        #         # Valid Login
        #
        parabank.login_details("john", "demo")

        profile = ProfileUpdate(driver)
        profile.click_update_profile_link()

        profile.update_profile_info("saurabh", "k", "saint martha street", "NewYork",
                                    "Washington DC", "413431", "84234234")
        self.logger.info("profile update complete")
        time.sleep(3)
        profile.click_profile_button()

        self.logger.info("Parabank end-to-end test completed")
