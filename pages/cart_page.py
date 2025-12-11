# pages/cart_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class CartPage(BasePage):
    
    # Locators
    CART_LIST = (By.CLASS_NAME, "cart_list") 
    CART_ITEMS = (By.CLASS_NAME, "cart_item") 
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name") 
    
    # כפתורי Remove (לוקייטור גנרי לכולם)
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='remove-']")
    
    def get_cart_items(self):
        """מחזיר רשימה של כל האלמנטים של המוצרים שנמצאים בעגלה."""
        return self.find_all(self.CART_ITEMS)

    def get_cart_item_names(self):
        """מחזיר רשימת שמות של כל המוצרים בעגלה."""
        cart_list_element = self.find(self.CART_LIST) 
        name_elements = cart_list_element.find_elements(*self.CART_ITEM_NAMES)
        return [el.text for el in name_elements] 

    def remove_first_item(self):
        """
        מסיר את הפריט הראשון בעגלה.
        משתמש ב-JS Click כדי לוודא שהלחיצה נקלטת גם בעומס.
        """
        # מוצאים את כל כפתורי ה-Remove בדף
        buttons = self.find_all(self.REMOVE_BUTTONS)
        
        if buttons:
            # לחיצה חכמה באמצעות JS
            self.driver.execute_script("arguments[0].click();", buttons[0])
            
            # המתנה קריטית: נותנים לאתר שנייה לעדכן את העגלה ולמחוק את השורה
            time.sleep(1)