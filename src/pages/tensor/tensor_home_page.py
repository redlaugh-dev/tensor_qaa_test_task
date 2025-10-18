

from src.pages.tensor.tensor_base_page import TensorBasePage
from src.components.tensor.tensor_index_card_component import TensorIndexCardComponent
from selenium.webdriver.common.by import By 


class TensorHomePage(TensorBasePage):
    INDEX_CARD_BLOCKS = (By.CLASS_NAME, 'tensor_ru-Index__card')
    def __init__(self, browser):
        super().__init__(browser)
    
    def get_index_cards(self):
        elements = self.find_elements(*self.INDEX_CARD_BLOCKS)
        return list(map(lambda x: TensorIndexCardComponent(self.browser, x),elements))
