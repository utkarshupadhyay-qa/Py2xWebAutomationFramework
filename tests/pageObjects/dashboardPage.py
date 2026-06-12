# Dashboard Class
# Responsibilities -> Verify the username

# Page Class
# Page Actions

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    # Page Locators
    user_logged_in = (By.XPATH, "//h4[contains(text(),'Set Up Your Account')]")

    # Page Action
    def get_user_logged_in(self):
        return WebDriverWait(driver=self.driver, timeout=10).until(
            EC.visibility_of_element_located(
                self.user_logged_in
            )
        )
        # return self.driver.find_element(*DashboardPage.user_logged_in)

    # Page Action (Main Action)
    def user_logged_in_text(self):
        return self.get_user_logged_in().text