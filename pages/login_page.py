# pages/login_page.py
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    URL = "https://www.saucedemo.com/"

    # לוקייטורים
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    @allure.step("פתיחת דף הלוגין")
    def open(self):
        self.driver.get(self.URL)

    @allure.step("ביצוע לוגין עם המשתמש: {username}")
    def login(self, username, password):
        self.open()
        self.write(self.USERNAME, username)
        self.write(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    @allure.step("קבלת הודעת שגיאה")
    def get_error_message(self):
        return self.get_text(self.ERROR_MSG)