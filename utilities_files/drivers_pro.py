from selenium import webdriver as wv #web driver
from selenium.webdriver.chrome.service import Service #service object
from webdriver_manager.chrome import ChromeDriverManager as ch #chrime driver 
import pytest as po

@po.fixture
def setup():
    return wv.Chrome(service=Service(executable_path=ch().install()))
