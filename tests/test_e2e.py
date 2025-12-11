# tests/test_e2e.py
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_full_purchase_flow(driver):
    """
    תרחיש קצה-לקצה מלא (E2E):
    1. התחברות למערכת
    2. הוספת מוצר לעגלה
    3. מעבר לעגלה ולחיצה על Checkout
    4. מילוי פרטים אישיים
    5. סיום הזמנה ואימות הודעת הצלחה
    """
    
    # 1. Login
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    # 2. Add product to cart
    home_page = HomePage(driver)
    home_page.add_product_to_cart_by_index(0) # מוסיפים את המוצר הראשון
    
    # 3. Go to cart & Proceed to Checkout
    home_page.go_to_cart()
    
    cart_page = CartPage(driver)
    # אנחנו צריכים ללחוץ על checkout. 
    # הערה: כפתור ה-checkout נמצא בעמוד העגלה.
    # אפשר להשתמש ב-CheckoutPage כדי למצוא אותו או להוסיף ל-CartPage.
    # לשם הפשטות, נשתמש ב-CheckoutPage שמכיל את ה-Locator הזה.
    checkout_page = CheckoutPage(driver)
    checkout_page.click_checkout()
    
    # 4. Fill details
    checkout_page.fill_details("Dana", "Tester", "12345")
    checkout_page.click_continue()
    
    # (כאן אפשר להוסיף בדיקת ביניים של עמוד הסיכום אם רוצים)
    
    # 5. Finish & Validate
    checkout_page.click_finish()
    
    success_msg = checkout_page.get_success_message()
    assert "Thank you for your order!" in success_msg