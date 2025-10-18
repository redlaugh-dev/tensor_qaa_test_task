from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, browser):
        self.browser = browser
    
    def find(self, *args):
        return self.browser.find_element(*args)
    
    def find_elements(self, *args):
        return self.browser.find_elements(*args)
    
    