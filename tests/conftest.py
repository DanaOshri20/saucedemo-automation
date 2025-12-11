# conftest.py
import pytest
from utils.driver_factory import create_driver

@pytest.fixture
def driver():
    driver = create_driver()
    driver.maximize_window()  #מגדיל את המסך כדי שכל האלמנטים יהיו גלויים
    yield driver
    try:
        # ניקוי Local Storage כדי להבטיח טסטים נקיים
        driver.execute_script("window.localStorage.clear();")
    except:
        pass
    driver.quit()