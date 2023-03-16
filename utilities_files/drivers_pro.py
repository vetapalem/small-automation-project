from selenium import webdriver as wv
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager as ch
import pytest as po

@po.fixture
def setup():
    return wv.Chrome(service=Service(executable_path=ch().install()))