from src.components.saby.saby_partners_list_component import SabyPartnersListComponent
from src.pages.saby.saby_base_page import SabyBasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.tensor.tensor_home_page import TensorHomePage

class SabyContactsPage(SabyBasePage):
    TENSOR_LOGO_LINK = (By.CSS_SELECTOR, "a[href='https://tensor.ru/']")
    REGION = (By.CLASS_NAME, 'sbis_ru-Region-Chooser__text')
    PARTHNERS_LIST = (By.CSS_SELECTOR, "div[data-qa='items-container']")
    CHANGE_REGION_DIALOG = (By.NAME, 'dialog')
    
    def __init__(self, browser):
        super().__init__(browser)
    
    def open(self):
        self.browser.get("")
        self.wait_loadingOverlay()

    def tensor_logo_click(self):
        windows = self.browser.window_handles;
        tensor_logo_link = self.find(*self.TENSOR_LOGO_LINK)
        tensor_logo_link.click()
        WebDriverWait(self.browser, 5).until(EC.new_window_is_opened(windows))
        self.browser.switch_to.window(self.browser.window_handles[-1])
        tensor_home_page = TensorHomePage(self.browser)
        tensor_home_page.wait_loadingOverlay()
        return tensor_home_page
    
    @property
    def current_region(self):
        return self.find(*self.REGION).text
    
    @property
    def partners_list_component(self):
        return SabyPartnersListComponent(self.browser, self.find(*self.PARTHNERS_LIST))

    def change_region(self, region):
        self.find(*self.REGION).click()
        change_region_dialog = WebDriverWait(self.browser,5).until(EC.element_to_be_clickable(self.CHANGE_REGION_DIALOG))
        region_locator = (By.CSS_SELECTOR, f"span.sbis_ru-link[title='{region}']")
        change_region_dialog.find_element(*region_locator).click()
        WebDriverWait(self.browser,5).until(EC.text_to_be_present_in_element(self.REGION,region))
