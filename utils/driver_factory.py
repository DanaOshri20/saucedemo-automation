# utils/driver_factory.py
from selenium import webdriver
from config.config import Config

def create_driver():
    options = webdriver.ChromeOptions()
    
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2
    }
    options.add_experimental_option("prefs", prefs)
    
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    
    # במקום maximize (שלא תמיד עובד ב-headless), אנחנו קובעים גודל קבוע.
    options.add_argument("--window-size=1920,1080")

    if Config.HEADLESS:
        options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    
    return driver