# tests/test_cart.py
from pages.login_page import LoginPage       # לוגין
from pages.home_page import HomePage         # דף מוצרים
from pages.product_page import ProductPage   # דף מוצר
from pages.cart_page import CartPage         # דף עגלה


def login_add_two_products_and_go_to_cart(driver):
    """
    1. לוגין
    2. מוסיפה שני מוצרים לעגלה מדף המוצרים (לפי הרשימה)
    3. נכנסת לעגלת הקניות
    מחזירה: cart_page, selected_names
    """
    # לוגין
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    home_page = HomePage(driver)

    # לוקחים את רשימת שמות המוצרים ומבחרים את שני הראשונים
    all_names = home_page.get_all_product_names()
    selected_names = all_names[0:2]

    # מוסיפים שני מוצרים לעגלה לפי אינדקס ברשימה
    home_page.add_product_to_cart_by_index(0)
    home_page.add_product_to_cart_by_index(1)

    # עוברים לעגלת הקניות
    home_page.go_to_cart()
    cart_page = CartPage(driver)

    return cart_page, selected_names

def test_cart_items_count_after_adding_two_products(driver):
    """
    בדיקה שלאחר הוספת שני מוצרים – יש 2 מוצרים בעגלה.
    """
    cart_page, selected_names = login_add_two_products_and_go_to_cart(driver)

    cart_items = cart_page.get_cart_items()  # רשימת פריטים בעגלה
    assert len(cart_items) == 2              # מצפים ל-2


def test_cart_item_names_match_selected(driver):
    """
    בדיקה ששמות המוצרים בעגלה תואמים לשמות שבחרנו מדף המוצרים.
    """
    cart_page, selected_names = login_add_two_products_and_go_to_cart(driver)

    cart_names = cart_page.get_cart_item_names()

    # משווים כסטים כדי שסדר לא ישנה
    assert set(cart_names) == set(selected_names)


def test_remove_item_from_cart(driver):
    """
    בדיקה שמחיקת מוצר אחד מעדכנת את מספר הפריטים בעגלה.
    """
    cart_page, selected_names = login_add_two_products_and_go_to_cart(driver)

    # לפני מחיקה: 2 מוצרים
    assert len(cart_page.get_cart_items()) == 2

    # מסירים מוצר אחד
    cart_page.remove_first_item()

    # בודקים שנשאר רק אחד
    remaining_items = cart_page.get_cart_items()
    assert len(remaining_items) == 1
