#coding=utf-8
from appium import webdriver
from time import sleep
import re
import os

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2' # 要跟模拟器版本完全一致
desired_caps['noReset'] = True
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.shizhuang.duapp'
desired_caps['appActivity'] = 'com.shine.ui.home.SplashActivity'

os.system("adb\\adb connect 127.0.0.1:62001")

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

x = 720
y = 1280
header = 146
goodItem = 354

def tabShose():
  driver.find_element_by_android_uiautomator('text("球鞋")').click()

def tap1():
  driver.tap([(x / 4,     header + goodItem/2)], 500)
def tap2():
  driver.tap([(x / 4 * 3, header + goodItem/2)], 500)
def tap3():
  driver.tap([(x / 4,     header + goodItem/2 * 3)], 500)
def tap4():
  driver.tap([(x / 4 * 3, goodItem/2 * 3)], 500)
def tap5():
  driver.tap([(x / 4,     header + goodItem/2 * 5)], 500)
def tap6():
  driver.tap([(x / 4 * 3, header + goodItem/2 * 5)], 500)

taps = [tap1, tap2, tap3, tap4, tap5, tap6]

def swipePage():
  driver.swipe(x/2, 1000, x/2, header)

def back():
  os.system("adb\\adb shell input keyevent 4")

def visiblityAllSold():
  # 向上滑动，购买记录元素可视
  driver.swipe(360, 700, 360, 246, 500)

def soldNum():
  soldNumTxt = driver.find_element_by_id('com.shizhuang.duapp:id/tv_sold_num').get_attribute('text')
  print(soldNumTxt)
  # 购买记录总条数
  soldNum = re.findall('\d+',soldNumTxt)[0]
  return int(soldNum)
def gotoAllSold():
  sn = soldNum()
  pageSize = 20
  pageVisibilite = 12
  allEl = driver.find_element_by_id('com.shizhuang.duapp:id/tv_sold_all')
  if (allEl):
    allEl.click()
    #count = int(sn / pageVisibilite) + 1
    count = 5
    for i in range(count):
      swipePage()
      sleep(3)
    back()

def loop():
  for i in range(len(taps)):
    taps[i]()
    sleep(1)
    visiblityAllSold()
    sleep(1)
    gotoAllSold()
    sleep(1)
    back()
    sleep(1)
def start():
  
  tabShose()

  while(True):
    loop()
    swipePage()
    sleep(3)

# 等待启动完成。应该精准判断Activity的状态，还没查资料，偷懒直接sleep!!!
sleep(5)
start()