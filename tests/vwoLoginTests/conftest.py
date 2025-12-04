from selenium import webdriver
from selenium.webdriver import Chrome
import pytest

# WebDriver fixture example
import os
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="class")   # Scope = class (because this function will be used by a CLASS)
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    username = os.getenv("NAME")
    password = os.getenv("PASSWORD")
    base_url = os.getenv("BASE_URL")
    katalon_url = os.getenv("KATALON_URL")
    hr_url = os.getenv("HR_APP_URL")

    request.cls.driver = driver  # cls will help us to use this variable in "test_vwologin_pom.py" -> use this in class
    request.cls.username = username
    request.cls.password = password
    request.cls.base_url = base_url
    request.cls.katalon_url = katalon_url
    request.cls.hr_url = hr_url

    yield driver # This is signal to Python interpreter -> to tell driver to stop after sometime -> quit
    driver.quit()





@pytest.fixture(scope="class")
def connect_to_db(request):
    pass


@pytest.fixture(scope="class")
def connect_to_excel(request):
    pass