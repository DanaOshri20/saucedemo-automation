from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def login_and_go_to_home(driver):
    """פונקציית עזר – לוגין והגעה לדף המוצרים."""
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    return HomePage(driver)


def test_products_list_visible(driver):
    """
    בדיקה שיש בכלל מוצרים ברשימה אחרי לוגין.
    """
    home_page = login_and_go_to_home(driver)
    products = home_page.get_all_products()
    assert len(products) > 0


def test_product_details_name_matches(driver):
    """
    בדיקה שהשם של מוצר ברשימה תואם לשם בעמוד פרטי מוצר.
    """
    home_page = login_and_go_to_home(driver)

    names = home_page.get_all_product_names()
    first_name = names[0]

    home_page.open_first_product()
    product_page = ProductPage(driver)

    details_name = product_page.get_product_name()
    assert first_name == details_name


def test_add_to_cart_from_product_page(driver):
    """
    בדיקה שהוספת מוצר מתוך דף מוצר אכן מוסיפה אותו לעגלה.
    """
    home_page = login_and_go_to_home(driver)

    # בהתחלה העגלה אמורה להיות ריקה
    assert home_page.get_cart_count() == 0

    # נכנסים למוצר הראשון
    home_page.open_first_product()
    product_page = ProductPage(driver)

    # מוסיפים לעגלה מתוך דף מוצר
    product_page.add_to_cart()

    # חוזרים לרשימת מוצרים
    product_page.go_back_to_products()

    # יוצרים מחדש אובייקט HomePage (אחרי הניווט)
    home_page_after = HomePage(driver)

    # במקום לסמוך על הבאדג', נלך לעגלת הקניות ונבדוק שם
    home_page_after.go_to_cart()
    cart_page = CartPage(driver)

    # מצפים שיהיה מוצר אחד בעגלה
    assert len(cart_page.get_cart_items()) == 1
