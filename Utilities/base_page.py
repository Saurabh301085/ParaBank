from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class ParaBankWebElements:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def scroll_down_page(self):
        self.driver.execute_script("window.scrollBy(0,250);")

    def enter_text(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)
                        ).send_keys(text)

    def click_button(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)
                        ).click()

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)
                               ).text

    def clear_text(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator)
                        ).clear()

    # def clear_multiple_fields(self, locators):
    #     for locator in locators:
    #         element = self.wait.until(EC.visibility_of_element_located(locator))
    #         element.clear()

    def clear_multiple_fields(self, *locators):
        for locator in locators:
            self.clear_text(locator)

    def select_dropdown(self, locator, value):
        dropdown = Select(self.wait.until(EC.visibility_of_element_located(locator)))
        dropdown.select_by_value(value)

    def success_message(self, locator, expected_msg):
        return self.wait.until(EC.text_to_be_present_in_element(locator, expected_msg)
                               )

    # def take_screenshot(self, file_name):
    #     self.driver.save_screenshot(f"Screenshots/{file_name}.png")
    def take_screenshot(self, file_name):
        project_path = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        screenshot_path = os.path.join(
            project_path,
            "Screenshots",
            f"{file_name}.png"
        )

        self.driver.save_screenshot(screenshot_path)

        print(f"Screenshot saved: {screenshot_path}")