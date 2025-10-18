from src.components.base_component import BaseComponent
from selenium.webdriver.common.by import By

class SabyPartnersListComponent(BaseComponent):
    
    CITY = (By.ID, "city-id-2")
    PARTNER_NAME = (By.CLASS_NAME, "sbisru-Contacts-List__name")

    def __init__(self, browser, element):
        super().__init__(browser, element)
    
    @property
    def city(self):
        return self.find(*self.CITY).text

    @property
    def partners_names(self):
        return list(map(lambda x: x.text, self.find_elements(*self.PARTNER_NAME)))