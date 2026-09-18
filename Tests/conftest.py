from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    # options = Options()
    # options.binary_location=f"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
    # driver = webdriver.Chrome(options=options)
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    # driver.refresh()
    driver.maximize_window()

    yield driver
    driver.quit()
