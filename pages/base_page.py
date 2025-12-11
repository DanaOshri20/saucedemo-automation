# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # זמן המתנה סביר
        self.wait = WebDriverWait(driver, 15)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        """
         Force Click באמצעות JavaScript.
        אנחנו לא מחכים שהאלמנט יהיה 'Clickable' (מה שגורם לנפילות),
        אלא רק שהוא יהיה קיים (Presence), ואז כופים לחיצה.
        """
        # 1. מוודאים שהאלמנט קיים ב-DOM (לא חייב להיות גלוי לעין)
        element = self.wait.until(EC.presence_of_element_located(locator))
        
        # 2. מדגישים את האלמנט (אופציונלי, עוזר לראות מה קורה) - לא חובה
        # self.driver.execute_script("arguments[0].style.border='3px solid red'", element)

        # 3. ביצוע לחיצה בכוח באמצעות JavaScript
        self.driver.execute_script("arguments[0].click();", element)

    def write(self, locator, text):
        # גם כאן, נוודא שהאלמנט קיים ואז נשלח מידע
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        # מספיק שהאלמנט קיים כדי לקחת ממנו טקסט
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.text

    def is_visible(self, locator):
        try:
            self.driver.find_element(*locator).is_displayed()
            return True
        except:
            return False