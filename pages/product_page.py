# pages/product_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_details_name")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[id^='add-to-cart']")
    
    BACK_BUTTON = (By.ID, "back-to-products")

    def get_product_name(self):
        return self.get_text(self.PRODUCT_NAME)

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def go_back_to_products(self):
        self.click(self.BACK_BUTTON)