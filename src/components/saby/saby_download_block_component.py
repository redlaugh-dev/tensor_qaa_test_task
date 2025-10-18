import os
from src.components.base_component import BaseComponent
from selenium.webdriver.common.by import By
import re
from test.conftest import DOWNLOAD_DIR
from src.support.download_wait import download_wait

class SabyDownloadBlockComponent(BaseComponent):

    TITLE_DOWNLOAD_BLOCK = (By.CLASS_NAME, "sbis_ru-DownloadNew-h3")
    DOWNLOAD_LINK = (By.CLASS_NAME, "sbis_ru-DownloadNew-loadLink__link")

    def __init__(self, browser, element):
        super().__init__(browser, element)  

    @property
    def title(self):
        return self.find(*self.TITLE_DOWNLOAD_BLOCK).text
    
    @property 
    def size_file(self):
        link_text = self.find(*self.DOWNLOAD_LINK).text
        return next(iter(re.findall(r'\d*\.\d+',link_text)),None)
    
    @property
    def file_name(self):
        href = self.find(*self.DOWNLOAD_LINK).get_attribute('href')
        return href.split('/')[-1]
     
    def download_file(self):
        file_path = os.path.join(DOWNLOAD_DIR,self.file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
        self.find(*self.DOWNLOAD_LINK).click()
        download_wait(file_path=file_path,duration=30)
        return file_path