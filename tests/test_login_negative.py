import pytest
from utils.browser import create_driver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
import time

@pytest.mark.parametrize("username,password,expected", [
    ("", "", "Username is required"),
    ("standard_user", "", "Password is required"),
    ("", "secret_sauce", "Username is required"),
    ("salah_user", "salah_password", "Username and password do not match any user"),
    (" "*10, " "*10, "Username and password do not match"),
    ("!"*50, "@"*50, "Username and password do not match any user"),
    ("a"*300, "b"*300, "Username and password do not match any user")
])
def test_login_invalid_variations(username, password, expected):
    driver = create_driver()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")

    login = LoginPage(driver)
    login.input_username(username)
    login.input_password(password)
    login.click_login()

    time.sleep(1)
    error_text = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert expected.lower() in error_text.lower()
    driver.quit()
