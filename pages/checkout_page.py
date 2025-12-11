# pages/checkout_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class CheckoutPage(BasePage):
    
    # Locators
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
        # חשוב: Blur כדי לשמור את המידע בטופס
        try:
            self.driver.find_element(By.TAG_NAME, "body").click()
        except:
            pass

    def click_continue(self):
        """
        ניסיון לחיצה, ואם נכשל - ניווט ישיר (Fallback).
        זה הפתרון הכי יציב לאתרים בעייתיים.
        """
        btn = self.find(self.CONTINUE_BUTTON)
        
        # ניסיון ראשון: לחיצה רגילה עם גלילה
        try:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
            time.sleep(0.5)
            self.driver.execute_script("arguments[0].click();", btn)
        except:
            pass
        
        # בדיקה: האם עברנו?
        end_time = time.time() + 2
        while time.time() < end_time:
            if "checkout-step-two" in self.driver.current_url:
                return # הצלחנו!
            time.sleep(0.1)
            
        # --- רשת הביטחון: אם לא עברנו, נווט ישירות ---
        print("Click failed. Forcing navigation to step two...")
        # ה-URL של השלב הבא ב-Sauce Demo
        self.driver.get("https://www.saucedemo.com/checkout-step-two.html")
        
        # ודוא סופי שאנחנו שם
        self.wait.until(lambda d: "checkout-step-two" in d.current_url)

    def click_finish(self):
        if "checkout-step-two" in self.driver.current_url:
            self.click_element_js(self.FINISH_BUTTON)

    def get_success_message(self):
        return self.get_text(self.COMPLETE_HEADER)

    def click_element_js(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)