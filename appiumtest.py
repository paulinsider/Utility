#coding=utf-8
from appium import webdriver
from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2' # 要跟模拟器版本完全一致
desired_caps['noReset'] = True
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.shizhuang.duapp'
desired_caps['appActivity'] = 'com.shine.ui.home.SplashActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 等待启动完成。应该精准判断Activity的状态，还没查资料，偷懒直接sleep!!!
sleep(2)

# 用文本定位控件
driver.find_element_by_android_uiautomator('text("登录")').click()
driver.find_element_by_android_uiautomator('text("用密码登录")').click()
# 用id定位控件更精准
driver.find_element_by_id('et_username').send_keys("18801881888")
driver.find_element_by_id('et_password').send_keys("1234abcd")
driver.find_element_by_id('btn_sure').click()

sleep(3)

driver.quit()
