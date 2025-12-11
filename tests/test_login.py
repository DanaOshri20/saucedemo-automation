from pages.login_page import LoginPage

def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # אימות שהצלחנו להגיע לדף הבא
    assert "inventory" in driver.current_url


def test_login_wrong_password(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "aaaaaa")

    # בודקים שמופיעה שגיאה
    error = login_page.get_error_message()
    assert "Epic sadface" in error
