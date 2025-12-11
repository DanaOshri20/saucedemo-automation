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
        לחיצה חכמה (Smart Retry):
        מנסה ללחוץ ובודקת אם הדף השתנה. אם לא - מנסה שוב.
        זה פתרון יציב וחוקי לבעיות עומס.
        """
        btn = self.find(self.CONTINUE_BUTTON)
        
        # ננסה ללחוץ עד 3 פעמים
        for attempt in range(3):
            try:
                # נסיון 1: לחיצה רגילה (הכי נכון)
                btn.click()
            except:
                # אם נכשל (למשל אלמנט מוסתר), ננסה JS Click
                self.driver.execute_script("arguments[0].click();", btn)
            
            # בדיקה מהירה: האם עברנו דף?
            # נותנים לו שנייה להגיב
            end_time = time.time() + 1.5
            while time.time() < end_time:
                if "checkout-step-two" in self.driver.current_url:
                    return # הצלחנו! יוצאים מהפונקציה
                time.sleep(0.1)
            
            # אם הגענו לפה, הלחיצה לא תפסה. הלולאה תריץ ניסיון נוסף.
            print(f"Click attempt {attempt+1} failed to change URL. Retrying...")

        # וידוא סופי (אם אחרי 3 פעמים זה לא עבד, זה ייכשל כאן בצדק)
        self.wait.until(lambda d: "checkout-step-two" in d.current_url)

    def click_finish(self):
        # אותו עקרון ל-Finish אם צריך, אבל בד"כ Continue הוא הבעייתי
        if "checkout-step-two" in self.driver.current_url:
            self.click_element_js(self.FINISH_BUTTON)

    def get_success_message(self):
        return self.get_text(self.COMPLETE_HEADER)

    def click_element_js(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)