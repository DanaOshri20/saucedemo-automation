# pages/home_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class HomePage(BasePage):
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    INVENTORY_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_IMAGE_LINK = (By.CSS_SELECTOR, "div.inventory_item_img a")
    
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button.btn_inventory")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def get_all_products(self):
        return self.find_all(self.INVENTORY_ITEMS)

    def get_all_product_names(self):
        name_elements = self.find_all(self.INVENTORY_ITEM_NAMES)
        return [el.text for el in name_elements]

    def open_first_product(self):
        product_images = self.find_all(self.PRODUCT_IMAGE_LINK)
        self.click_element(product_images[0])
        self.wait.until(lambda d: "inventory-item" in d.current_url)

    def add_product_to_cart_by_index(self, index: int):
        """
        הוספת מוצר לעגלה בצורה חסינת-עומס.
        """
        buttons = self.find_all(self.ADD_TO_CART_BUTTONS)
        
        # 1. שימוש בלחיצה חכמה (JS) כדי לוודא שהלחיצה נקלטת גם בעומס
        self.click_element(buttons[index])
        
        # 2. המתנה קטנה כדי לוודא שהאתר הספיק לעדכן את העגלה לפני שממשיכים
        time.sleep(0.5)

    def go_to_cart(self):
        self.click(self.CART_ICON)

    def get_cart_count(self) -> int:
        try:
            count_element = self.find(self.CART_BADGE)
            return int(count_element.text)
        except:
            return 0
            
    def click_element(self, element):
        self.driver.execute_script("arguments[0].click();", element)