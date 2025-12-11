# pages/checkout_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):
    
    # Locators משודרגים ל-  data-test
    CHECKOUT_BUTTON = (By.ID, "checkout")
    
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_INPUT = (By.ID, "postal-code")
    
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-test='continue']")
    FINISH_BUTTON = (By.CSS_SELECTOR, "[data-test='finish']")
    
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    # Actions
    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def fill_details(self, first_name, last_name, zip_code):
        self.write(self.FIRST_NAME_INPUT, first_name)
        self.write(self.LAST_NAME_INPUT, last_name)
        self.write(self.ZIP_INPUT, zip_code)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def click_finish(self):
        self.click(self.FINISH_BUTTON)

    def get_success_message(self):
        return self.get_text(self.COMPLETE_HEADER)