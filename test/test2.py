# -*- coding: utf-8 -*-
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


phantomJSdriver = 'C:\\Users\\JiaLong\\PycharmProjects\\firstPythonProjects\\venv\\lib\\site-packages\\selenium\\webdriver\\phantomjs'
os.environ["webdriver.phantomjs.driver"] = phantomJSdriver
driver = webdriver.PhantomJS(phantomJSdriver)
driver.get("https://gateway.v2.cloopm.com/oauth/login")

# 输入账号密码
driver.find_element_by_name("username").send_keys("jialong.tian@hand-china.com")
driver.find_element_by_name("password").send_keys("lEstat147156!")

# 模拟点击登录
driver.find_element_by_xpath("//input[@class='input-submit login-btn']").click()

# 等待3秒
time.sleep(3)

# 生成登陆后快照
driver.save_screenshot("renren.png")