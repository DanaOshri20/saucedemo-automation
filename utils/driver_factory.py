# utils/driver_factory.py
from selenium import webdriver
# מחקנו את השורה של webdriver_manager וה-Service כי הם אלו שנתקעים
from config.config import Config

def create_driver():
    options = webdriver.ChromeOptions()
    
    # הגדרות לביטול התראות וסיסמאות
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2
    }
    options.add_experimental_option("prefs", prefs)
    
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")

    if Config.HEADLESS:
        options.add_argument("--headless")

    # --- התיקון כאן ---
    # במקום להשתמש ב-ChromeDriverManager().install() שנתקע,
    # אנחנו נותנים לסלניום לנהל את זה לבד (עובד בגרסאות חדשות),
    # או שהוא ישתמש במה שכבר מותקן לו.
    driver = webdriver.Chrome(options=options)
    
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    
    return driver