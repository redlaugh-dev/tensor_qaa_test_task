from selenium.webdriver.common.by import By
from src.pages.saby.saby_base_page import SabyBasePage
from src.pages.saby.saby_download_page import SabyDownloadPage
from src.components.saby.saby_contacts_component import SabyContactsComponent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SabyHomePage(SabyBasePage):

    CONTACTS_MENU_ITEM = (By.CSS_SELECTOR, 'li.sbisru-Header__menu-item-1')
    CONTACTS_MENU = (By.CLASS_NAME, 'sbisru-Header-ContactsMenu__items')
    DOWNLOAD_LINK = (By.CSS_SELECTOR, "a[href='/download']")

    def __init__(self, browser):
        super().__init__(browser)
    
    def open_page(self):
        self.browser.get('https://saby.ru')
        self.wait_loadingOverlay()
        return self

    def contacts_click(self):
        self.find(*self.CONTACTS_MENU_ITEM).click()
        contacts_menu = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located(self.CONTACTS_MENU))
        return SabyContactsComponent(self.browser, contacts_menu)
    
    def download_link_click(self):
        self.find(*self.DOWNLOAD_LINK).click()
        downlod_page = SabyDownloadPage(self.browser)
        downlod_page.wait_loadingOverlay()
        return SabyDownloadPage(self.browser)
    