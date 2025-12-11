# pages/checkout_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

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
        # שימוש בקליק הרגיל והטוב שלנו (שמחכה ל-Visibility)
        self.click(self.CHECKOUT_BUTTON)

    def fill_details(self, first_name, last_name, zip_code):
        """
        מילוי פרטים בצורה בטוחה עם וריפיקציה.
        """
        # מילוי רגיל
        self.write(self.FIRST_NAME_INPUT, first_name)
        self.write(self.LAST_NAME_INPUT, last_name)
        self.write(self.ZIP_INPUT, zip_code)
        
        # --- שלב האימות (Real World Practice) ---
        # אנחנו בודקים שהדפדפן אכן קלט את הערך בשדה האחרון.
        # אם זה ריק משום מה, נמלא שוב.
        input_value = self.find(self.ZIP_INPUT).get_attribute("value")
        if not input_value:
            self.write(self.ZIP_INPUT, zip_code)

    def click_continue(self):
        """
        לחיצה על Continue והמתנה למעבר דף.
        """
        self.click(self.CONTINUE_BUTTON)
        
        # אנחנו מצפים לעבור לדף step-two.
        # ה-wait כאן הוא הדבר הנכון לעשות.
        self.wait.until(lambda d: "checkout-step-two" in d.current_url)

    def click_finish(self):
        # וידוא שאנחנו בדף הנכון לפני לחיצה
        if "checkout-step-two" in self.driver.current_url:
            self.click(self.FINISH_BUTTON)

    def get_success_message(self):
        return self.get_text(self.COMPLETE_HEADER)