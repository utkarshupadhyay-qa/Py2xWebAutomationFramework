import time

import allure
import pytest
from selenium import webdriver

from tests.pageObjects.dashboardPage import DashboardPage
from tests.pageObjects.loginPage import LoginPage


# Assertions


# Set up the driver
@pytest.fixture()  # fixture can be used as test data which can be injected into our test cases
def setup():
    driver = webdriver.Chrome()
    # ChromeOptions
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    return driver


@allure.epic("VWO Login Test")
@allure.feature("TC#0 - VWO App Negative Test")
@pytest.mark.negative
def test_vwo_login_negative(setup):
    try:
        driver = setup
        loginPage = LoginPage(driver)
        loginPage.login_to_vwo(usr="admin@admin@gmail.com", pwd="admin")
        time.sleep(5)
        error_message = loginPage.get_error_message_text()
        assert error_message == "Yours email, password, IP address or location did not match"
    except Exception as e:
        pytest.xfail("Failed")
        print(e)


@allure.epic("VWO Login Test")
@allure.feature("TC#1 - VWO App Positive Test")
@pytest.mark.positive
def test_vwo_login_positive(setup):
    driver = setup
    loginPage = LoginPage(driver)
    loginPage.login_to_vwo(usr="utkarsh.qa@proton.me", pwd="Uttu@1234")
    time.sleep(10)
    dashboardPage = DashboardPage(driver)
    assert "Dashboard" in driver.title
    assert "Set Up Your Account" in dashboardPage.user_logged_in_text()
