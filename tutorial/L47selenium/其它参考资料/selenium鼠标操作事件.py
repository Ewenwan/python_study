# coding:utf-8
# __author__ = 'Gao'

# 鼠标操作事件：点击，右击，双击，拖动，移动，拖放等事件。
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

# 模拟鼠标右击事件
# img = driver.find_element_by_css_selector('#lg > img')

# 创建ActionChains()类的对象，需要参数driver。context_click右击事件
# action = ActionChains(driver).context_click(img)
# 当调用context_click()等相关的鼠标函数时，这些事件并不会立即执行，而是将所有的鼠标操作事件放入了一个队列中，当执行perform函数时，所有的鼠标操作事件才会被执行。
# action.perform()

# 鼠标双击
# ActionChains(driver).double_click(img).perform()

# 拖拽事件
action = ActionChains(driver)
# action.drag_and_drop('要移动的元素', '目标元素位置') # 将某一个元素拖动到某一个位置
# action.move_to_element('目标元素位置') # 将鼠标移动到某一个目标元素位置

menu = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_class_name('bri'))

print menu

action.move_to_element(menu).perform()

time.sleep(3)

driver.find_element_by_name('tj_img').click()
