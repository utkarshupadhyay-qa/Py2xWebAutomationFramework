# Login Page Class

# Responsibilities ->
# get username and send keys - email
# # get password and send keys - password
# # click the submit button and navigate to dashboard Page
# For Invalid creds. -> error message
# Forgot password


# Page Class contains:

# Page Locators
# Page Actions
# WebDriver Initializations
# Custom Functions also can be created
# No assertions(in Page Object Class)


from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):  # parameterise constructor
        self.driver = driver

    # Page Locators ( from app.vwo.com)

    username = (By.ID, "login-username")  # getting locator from app.vwo.com/login
    password = (By.NAME, "password")
    submit_button = (By.XPATH, "//button[@id='js-login-btn']")
    # forgot_password_button = (By.XPATH, "//button[normalize-space()='Forgot Password?']")
    error_message = (By.XPATH, "//div[@id='js-notification-box-msg]")
    free_trial = (By.XPATH, "//a[normalize-space()='Start a free trial']")

    # sso_login = (By.XPATH, "//button[normalize-space()='Sign in using SSO']")
    # remember_checkbox = (By.XPATH, "//label[@for='checkbox-remember']//span[@class='checkbox-radio-button ng-scope']//*[name()='svg']")

    # Note - Page Locators are just normal tuples , we need to make them into actions, so Page Actions are needed.
    # So that we can interact with them in future

    # Page Actions
    def get_username(self):
        return self.driver.find_element(*LoginPage.username)  # * means current class -> current_class.username

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)

    def get_error_message(self):
        return self.driver.find_element(*LoginPage.error_message)

    def get_free_trial(self):
        return self.driver.find_element(*LoginPage.free_trial)

    # Page object class - says that if you are not using any component as of now so don't use it
    # That's why we have commented forgot_password,sso_login,remember_me

    # Page Action - Main Action(login)

    def login_to_vwo(self, usr, pwd):
        self.get_username().send_keys(usr)
        self.get_password().send_keys(pwd)
        self.get_submit_button().click()

    # def login_to_vwo(self, usr, pwd, iserror):
    #     if iserror is True:
    #         self.get_username().send_keys("wrong")
    #         self.get_password().send_keys("wrong")
    #         self.get_submit_button().click()

    def get_error_message_text(self):
        return self.get_error_message().text

    def click_free_trial(self):
        self.get_free_trial()
