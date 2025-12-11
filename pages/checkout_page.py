# pages/checkout_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class CheckoutPage(BasePage):
    
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-test='continue']")
    FINISH_BUTTON = (By.CSS_SELECTOR, "[data-test='finish']")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def click_checkout(self):
        self.click_element_js(self.CHECKOUT_BUTTON)

    def fill_details(self, first_name, last_name, zip_code):
        self.write(self.FIRST_NAME_INPUT, first_name)
        self.write(self.LAST_NAME_INPUT, last_name)
        self.write(self.ZIP_INPUT, zip_code)

    def click_continue(self):
        """
        מנגנון חכם: מנסה ללחוץ ולוודא מעבר, עד 3 פעמים.
        """
        btn = self.find(self.CONTINUE_BUTTON)
        
        # לולאה שמנסה עד 3 פעמים
        for i in range(3):
            self.driver.execute_script("arguments[0].click();", btn)
            time.sleep(2) # נותנים לאתר 2 שניות להגיב
            
            if "checkout-step-two" in self.driver.current_url:
                return # הצלחנו! יוצאים מהפונקציה
            
            print(f"Retry {i+1}: Click didn't work, trying again...")
        
        # אם הגענו לפה, זה נכשל 3 פעמים - ניתן ל-Wait לזרוק את השגיאה
        self.wait.until(lambda d: "checkout-step-two" in d.current_url)

    def click_finish(self):
        btn = self.find(self.FINISH_BUTTON)
        self.driver.execute_script("arguments[0].click();", btn)

    def get_success_message(self):
        return self.get_text(self.COMPLETE_HEADER)

    def click_element_js(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)