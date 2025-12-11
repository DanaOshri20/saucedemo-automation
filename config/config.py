import os

class Config:
    """
    מחלקת הגדרות ראשית לפרויקט.
    כאן אנחנו שומרים את כל הקבועים (Constants).
    """
    
    # כתובת האתר הנבדק
    BASE_URL = "https://www.saucedemo.com"
    
    # דפדפן (אפשר לשנות ל-firefox בעתיד אם רוצים)
    BROWSER = "chrome"
    
    # האם להריץ בלי לראות את הדפדפן (Headless)?
    # כרגע False כדי שתראי מה קורה על המסך
    HEADLESS = False

    # זמן המתנה דיפולטיבי (בשניות) לאלמנטים
    IMPLICIT_WAIT = 10
    
    # פרטי התחברות (אפשר לשמור כאן או במשתני סביבה)
    STANDARD_USER = "standard_user"
    PASSWORD = "secret_sauce"