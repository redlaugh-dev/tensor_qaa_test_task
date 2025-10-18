import os
from src.pages.saby.saby_home_page import SabyHomePage




def test_scenario_3(browser):
    saby_dowload_page = SabyHomePage(browser).open_page().download_link_click()
    download_blocks = saby_dowload_page.dowload_blocks
    find_program = "Веб-установщик"
    program = next((x for x in download_blocks if x.title == find_program),None)
    assert program != None, "Искомый продукт отсуствует на странице"
    size_file = program.size_file
    file_path = program.download_file()
    assert f"{(os.path.getsize(file_path) / 1048576):.2f}" == size_file, 'Размер скачанного файла не совпадает с размером на сайте'

