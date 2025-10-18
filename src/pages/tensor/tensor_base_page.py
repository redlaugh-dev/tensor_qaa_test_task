
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By 


class TensorBasePage(BasePage):
    LOADING_OVERLAY = (By.NAME,'loadingOverlay')
    def __init__(self, browser):
        super().__init__(browser)
    
    def wait_loadingOverlay(self):
        WebDriverWait(self.browser, 10).until(EC.invisibility_of_element_located(self.LOADING_OVERLAY))