from src.pages.saby.saby_home_page import SabyHomePage

def test_scenario_2(browser):
    saby_contacts_panel = SabyHomePage(browser).open_page().contacts_click()
    saby_contacts_page = saby_contacts_panel.more_offices_click()
    yar_region = 'Ярославская обл.'
    assert yar_region == saby_contacts_page.current_region, 'Ожидаемый регион и регион страницы не совпадают'
    partners_component = saby_contacts_page.partners_list_component
    yar_partners_names = partners_component.partners_names
    assert len(yar_partners_names) > 0 , 'Список партнеров отсуствует'
    find_region = "Камчатский край"
    find_region_url_info = "41-kamchatskij-kraj"
    saby_contacts_page.change_region(find_region)
    assert saby_contacts_page.current_region == find_region, 'Регион не поменялся'
    assert saby_contacts_page.partners_list_component.partners_names != yar_partners_names, 'Список партнеров не поменялся'
    assert browser.title[16:] == find_region, 'Регион в заголовке страницы не соответствует выбранному региону'
    assert browser.current_url.find(find_region_url_info) > -1, 'Регион в заголовке страницы не соответствует выбранному региону'
