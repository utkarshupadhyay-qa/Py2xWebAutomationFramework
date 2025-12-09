from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
import time


@given("I am on the Google Page")   # it should be same heading as .feature file heading
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.get("https://www.google.com")
    time.sleep(2)


@when('I search for "{search_term}"')
def step_impl(context,search_term):
    search_box = context.browser.find_element(By.NAME, 'q')
    search_box.send_keys(search_term)
    search_box.submit()
    time.sleep(2)


@then('I should see "{expected_term}" in the results')
def step_impl(context,expected_term):
    assert expected_term in context.browser.page_source
    context.browser.quit()