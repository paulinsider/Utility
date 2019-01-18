#coding=utf-8
from appium import webdriver
from time import sleep
import re

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2' # 要跟模拟器版本完全一致
desired_caps['noReset'] = True
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.shizhuang.duapp'
desired_caps['appActivity'] = 'com.shine.ui.home.SplashActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 等待启动完成。应该精准判断Activity的状态，还没查资料，偷懒直接sleep!!!
sleep(5)
# top
# driver.swipe(360, 500, 360, 146, 500)
# left
# driver.swipe(620, 500, 320, 500, 500)
# driver.swipe(620, 500, 320, 500, 500)
# driver.swipe(620, 500, 320, 500, 500)
x = 720
y = 1280
header = 146
goodItem = 354

driver.find_element_by_android_uiautomator('text("球鞋")').click()

def tap1()
  driver.tap([(x / 4,     header + goodItem/2)], 500)
def tap2()
  driver.tap([(x / 4 * 3, header + goodItem/2)], 500)
def tap3()
  driver.tap([(x / 4,     header + goodItem/2 * 3)], 500)
def tap4()
driver.tap([(x / 4 * 3, goodItem/2 * 3)], 500)
def tap5()
  driver.tap([(x / 4,     header + goodItem/2 * 5)], 500)
def tap6()
  driver.tap([(x / 4 * 3,     header + goodItem/2 * 5)], 500)

def swipePage()
  driver.swipe(x/2, 1000 x/2, header)

def back()
  driver.keyevent('4')

def visiblityAllSold()
  # 向上滑动，购买记录元素可视
  driver.swipe(360, 500, 360, 146, 500)

sleep(2)
def soldNum()
  soldNumTxt = driver.find_element_by_id('com.shizhuang.duapp:id/tv_sold_num').get_attribute('text')
  # 购买记录总条数
  soldNum = re.findall('\d+',soldNumTxt)[0]
  return soldNum
def gotoAllSold
driver.find_element_by_id('com.shizhuang.duapp:id/tv_sold_all').click()


# # 用文本定位控件
# driver.find_element_by_android_uiautomator('text("登录")').click()
# driver.find_element_by_android_uiautomator('text("用密码登录")').click()
# # 用id定位控件更精准
# driver.find_element_by_id('et_username').send_keys("18801881888")
# driver.find_element_by_id('et_password').send_keys("1234abcd")
# driver.find_element_by_id('btn_sure').click()

# sleep(3)

# driver.quit()
