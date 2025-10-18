from src.pages.saby.saby_home_page import SabyHomePage
from src.pages.tensor.tensor_about_page import TensorAboutPage

def test_scenario_1(browser):
    saby_contacts_panel = SabyHomePage(browser).open_page().contacts_click()
    saby_contacts_page = saby_contacts_panel.more_offices_click()
    tensor_home_page = saby_contacts_page.tensor_logo_click()
    index_cards = tensor_home_page.get_index_cards()
    required_card_title = "Сила в людях"
    required_card = next((x for x in iter(index_cards) if x.title == required_card_title),None)
    assert required_card != None, 'Блок с указанным заголовком не найден'
    required_card.click_more_details()
    tensor_about_page = TensorAboutPage(browser)
    tensor_about_page.wait_loadingOverlay()
    assert browser.current_url == "https://tensor.ru/about", "URL страницы не соответствует ожидаемому результату"
    images = tensor_about_page.about_block_3.images
    assert len(images) > 0, 'В блоке 3 отсуствуют изображения'
    width = images[0].get_attribute('width')
    height = images[0].get_attribute('height')
    assert all(x.get_attribute('width') == width and x.get_attribute('height') == height for x in images[1:])

