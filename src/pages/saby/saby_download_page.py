from src.components.saby.saby_download_block_component import SabyDownloadBlockComponent
from src.pages.saby.saby_base_page import SabyBasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SabyDownloadPage(SabyBasePage):
    PRODUCTS_PANEL = (By.NAME, "TabButtons")
    DOWNLOAD_BLOCK = (By.CLASS_NAME, "sbis_ru-DownloadNew-block")
    SELECTED_SWITCHABLE_AREA = (By.CSS_SELECTOR, ".ws-SwitchableArea.ws-has-focus")
    SELECTED_SWITCHABLE_AREA_ITEM = (By.CSS_SELECTOR, ".ws-SwitchableArea__item.ws-has-focus")
    
    def __init__(self, browser):
        super().__init__(browser)

    def wait_loadingOverlay(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.SELECTED_SWITCHABLE_AREA))

    def select_product(self,id_product):
        current_url = self.browser.current_url
        products_panel = self.find(*self.PRODUCTS_PANEL)
        item_locator = (By.CSS_SELECTOR, f"div.controls-TabButton[data-id='{id_product}']")
        products_panel.find_element(*item_locator).click()
        WebDriverWait(self.browser,5).until(EC.url_changes(current_url))

    @property
    def dowload_blocks(self):
       area = self.find(*self.SELECTED_SWITCHABLE_AREA)
       item = area.find_element(*self.SELECTED_SWITCHABLE_AREA_ITEM)
       return list(map(lambda x: SabyDownloadBlockComponent(self.browser, x), item.find_elements(*self.DOWNLOAD_BLOCK)))
    

