from src.components.base_component import BaseComponent
from selenium.webdriver.common.by import By


class TensorAboutBlock3(BaseComponent):

    ABOUT_BLOCK_3_IMAGE = (By.CLASS_NAME, "tensor_ru-About__block3-image")
    
    def __init__(self, browser, element):
        super().__init__(browser, element)
    
    @property
    def images(self):
        return self.find_elements(*self.ABOUT_BLOCK_3_IMAGE)
