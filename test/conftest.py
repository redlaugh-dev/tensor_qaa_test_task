import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DOWNLOAD_DIR = os.path.join(os.getcwd(),"test")

@pytest.fixture()
def browser(): 
    options = Options()
    options.add_experimental_option('prefs', {
    'download.default_directory': DOWNLOAD_DIR,
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': True
    })
    edge = webdriver.Chrome(options=options)
    return edge