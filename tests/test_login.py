from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
import time

def test_login_valid():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")

    login = LoginPage(driver)
    login.input_username("standard_user")
    login.input_password("secret_sauce")
    login.click_login()

    time.sleep(2)
    assert "inventory" in driver.current_url
    driver.quit()

def test_login_invalid():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")

    login = LoginPage(driver)
    login.input_username("salah_user")
    login.input_password("salah_password")
    login.click_login()

    time.sleep(2)
    error_text = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Username and password do not match" in error_text
    driver.quit()
