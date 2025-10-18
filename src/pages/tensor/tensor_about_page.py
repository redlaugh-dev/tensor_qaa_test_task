from src.components.tensor.tensor_about_block_3 import TensorAboutBlock3
from src.pages.tensor.tensor_base_page import TensorBasePage
from selenium.webdriver.common.by import By


class TensorAboutPage(TensorBasePage):
    ABOUT_BLOCK_3 = (By.CLASS_NAME, "tensor_ru-About__block3")

    def __init__(self, browser):
        super().__init__(browser)
    
    @property
    def about_block_3(self):
        element = self.find(*self.ABOUT_BLOCK_3)
        return TensorAboutBlock3(self.browser, element)
