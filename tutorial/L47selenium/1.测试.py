# coding:utf-8
__author__ = 'trc'

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
time.sleep(1)












browser.quit()