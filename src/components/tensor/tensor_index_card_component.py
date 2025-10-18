from src.components.base_component import BaseComponent
from selenium.webdriver.common.by import By


class TensorIndexCardComponent(BaseComponent):

    INDEX_CARD_TITLE = (By.CLASS_NAME, 'tensor_ru-Index__card-title')
    MORE_DETAILS_LINK = (By.CLASS_NAME, 'tensor_ru-Index__link')

    def __init__(self, browser, element):
        super().__init__(browser, element)
    
    @property
    def title(self):
        return self.find(*self.INDEX_CARD_TITLE).text
    
    def click_more_details(self):
        self.find(*self.MORE_DETAILS_LINK).click()