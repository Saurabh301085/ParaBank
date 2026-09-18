from Parabank.Utilities.base_page import ParaBankWebElements
from Parabank.Utilities.logger import get_logger
from selenium.webdriver.common.by import By


class ParaBankPayBill(ParaBankWebElements):
    #calling Logger
    logger = get_logger()

    #locating the path of locators
    bill_pay_link = (By.XPATH,"//a[normalize-space()='Bill Pay']")
    Payee_name = (By.NAME,"payee.name")
    Address = (By.NAME,"payee.address.street")
    City = (By.NAME, "payee.address.city")
    State = (By.NAME, "payee.address.state")
    ZipCode = (By.NAME,"payee.address.zipCode")
    Phone = (By.XPATH, "//input[@id='9fe37283-bc45-4c2d-b691-dcd56be42e53']")
    Account_no = (By.XPATH,"//input[@name='payee.accountNumber']")
    Verify_acc_no = (By.NAME,"verifyAccount")
    from_Acc_no = (By.XPATH, "//select[@name='fromAccountId']")
    Amount = (By.XPATH, "//input[@name='amount']")
    send = (By.XPATH, "//input[@value='Send Payment']")

    #creating methods for each locators
    def click_bill_pay_link(self):
        self.click_button(self.bill_pay_link)
    def bill_payment_form(self, name, addr, city_name, state_name, zip, mobile, acc_number, verify_acc_no,
                          from_account_number, amt):
        self.logger.info("Enter Payee Name")
        self.enter_text(self.Payee_name,name)

        self.logger.info("Enter Payee Address")
        self.enter_text(self.Address,addr)

        self.logger.info("Enter Payee City")
        self.enter_text(self.City,city_name)

        self.logger.info("Enter Payee State")
        self.enter_text(self.State,state_name)

        self.logger.info("Enter Payee Zipcode")
        self.enter_text(self.ZipCode,zip)

        # self.logger.info("Enter Payee Phone")
        # self.enter_text(self.Phone,mobile)

        self.logger.info("Enter Payee Account number")
        self.enter_text(self.Account_no,acc_number)

        self.logger.info("Enter Payee verify_acc_nmber")
        self.enter_text(self.Verify_acc_no,verify_acc_no)

        self.select_dropdown(self.from_Acc_no,from_account_number)

        self.logger.info("Enter Payee amount")
        self.enter_text(self.Amount,amt)

    def send_payment(self):
        self.logger.info("Enter send payment button")
        self.click_button(self.send)
