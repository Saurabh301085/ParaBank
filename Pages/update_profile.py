import time

from Parabank.Utilities.base_page import ParaBankWebElements
from Parabank.Utilities.logger import get_logger
from selenium.webdriver.common.by import By


class ProfileUpdate(ParaBankWebElements):
    profile_link = (By.XPATH, "//a[normalize-space()='Update Contact Info']")
    fname = (By.ID, "customer.firstName")
    lname = (By.ID, "customer.lastName")
    addr = (By.ID, "customer.address.street")
    city_name = (By.ID, "customer.address.city")
    state_name = (By.ID, "customer.address.state")
    zip = (By.ID, "customer.address.zipCode")
    phone = (By.ID, "customer.phoneNumber")
    profile_button = (By.XPATH, "//input[@value='Update Profile']")

    logger = get_logger()

    def click_update_profile_link(self):
        self.click_button(self.profile_link)

    def update_profile_info(self, firstname, lastname, address, city, state, zipcode,
                            phone_number):
        self.clear_multiple_fields(
            self.fname,
            self.lname,
            self.addr,
            self.city_name,
            self.state_name,
            self.zip,
            self.phone
        )

        self.logger.info("enter first name")
        self.enter_text(self.fname, firstname)

        self.logger.info("enter last name")
        self.enter_text(self.lname, lastname)

        self.logger.info("enter address")
        self.enter_text(self.addr, address)

        self.logger.info("enter city")
        self.enter_text(self.city_name, city)

        self.logger.info("enter state")
        self.enter_text(self.state_name, state)

        self.logger.info("enter zipcode")
        self.enter_text(self.zip, zipcode)

        self.logger.info("enter phone")
        self.enter_text(self.phone, phone_number)
        time.sleep(3)

    def click_profile_button(self):
        self.logger.info("hit the profile button")
        self.click_button(self.profile_button)
        self.take_screenshot("profile_updated")
