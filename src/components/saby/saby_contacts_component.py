
from selenium.webdriver.common.by import By
from src.components.base_component import BaseComponent
from src.pages.saby.saby_contacts_page import SabyContactsPage



class SabyContactsComponent(BaseComponent):

    MORE_OFFCES_LINK = (By.CSS_SELECTOR, "a[href='/contacts']")

    def __init__(self, browser, element):
        super().__init__(browser, element)
    
    def more_offices_click(self):
        self.find(*self.MORE_OFFCES_LINK).click()
        contactPage =  SabyContactsPage(self.browser)
        contactPage.wait_loadingOverlay()
        return contactPage

        