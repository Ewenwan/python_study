# coding:utf-8
# __author__ = 'Gao'
import time,os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get('https://pan.baidu.com/')

# 设置智能等待
# driver.implicitly_wait(3)
time.sleep(3)

# 定位 ‘账号密码登录’ 标签并点击
driver.find_element_by_id('TANGRAM__PSP_4__footerULoginBtn').click()

# 获取用户名和密码输入框，进行输入
username = driver.find_element_by_id('TANGRAM__PSP_4__userName')
# 清空默认信息
username.clear()
username.send_keys('13275975573')

password = driver.find_element_by_id('TANGRAM__PSP_4__password')
# 清空旧信息
password.clear()
password.send_keys('yuhao@0923')

# 定位到登录按钮
login_button = driver.find_element_by_id('TANGRAM__PSP_4__submit')
login_button.click()

# ------------- 登录成功 ---------------
# 定位上传按钮，将光标移动到上传按钮
upload = WebDriverWait(driver, 15).until(lambda driver:driver.find_element_by_id('h5Input0'))
ActionChains(driver).move_to_element(upload).perform()

# # 定位上传文件或者上传文件夹
input = driver.find_element_by_id('h5Input1').send_keys(os.path.abspath('C:/Users/ZhangYuHaoI/Desktop/test.txt'))
#
#
# # 如果需要操作本地窗口，可以借助autoit第三方开源库完成。

# print os.path.abspath('C:/Users/ZhangYuHaoI/Desktop/test.txt')

