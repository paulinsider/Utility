#coding=utf-8
from appium import webdriver
from time import sleep
import time
import re
import os

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2' # 要跟模拟器版本完全一致
desired_caps['noReset'] = True
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.nice.main'
desired_caps['appActivity'] = 'com.nice.main.activities.MainActivity_'

os.system("adb\\adb connect 127.0.0.1:62001")

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

x = 720
y = 1280
header = 240
offsetTop = 337
goodItem = 442
recordHeight = 88

def tabShose():
  driver.find_element_by_android_uiautomator('text("好货")').click()
  sleep(1)
  driver.find_element_by_android_uiautomator('text("球鞋")').click()

  

def tap1():
  driver.tap([(x / 4,     header + goodItem/2)], 500)
def tap2():
  driver.tap([(x / 4 * 3, header + goodItem/2)], 500)

taps = [tap1, tap2]



def back():
  os.system("adb\\adb shell input keyevent 4")

def visiblityAllSold():
  # 向上滑动，购买记录元素可视
  driver.swipe(x/2, y - 200, x/2, y - 200 - y * 2 / 3, 500)

def soldNum():
  snEl = driver.find_element_by_id('com.nice.main:id/tv_title')
  if (snEl):
    soldNumTxt = snEl.get_attribute('text')
    print(soldNumTxt)
    # 购买记录总条数
    soldNum = re.findall('\d+',soldNumTxt)[0]
    return int(soldNum)
  else:
    return 0
def gotoAllSold():
  # sn = soldNum()
  # pageSize = 20
  # pageVisibilite = 12
  # driver.swipe(x/2, y - 200 - y * 2 / 3, x/2, y - 200, 500)
  allEl = driver.find_element_by_id('com.nice.main:id/tv_all_deal')
  if (allEl):
    allEl.click()
    
    sleep(1) # 进入记录页等待数据加载完成
    for i in range(30):
      driver.swipe(x/2, y * 2 / 3, x/2, 200 , 500) # 上拉加载更多
      sleep(1)
      
    back()



def oneRowGood():
  for i in range(2):
    taps[i]()
    sleep(1)
    # visiblityAllSold()
    # sleep(1)
    gotoAllSold()
    sleep(1)
    back()
    sleep(1)

def run():
  tabShose()
  sleep(1)
  driver.swipe(x/2, offsetTop + goodItem + header, x/2, goodItem + header)
  sleep(1)
  while(True):
    
    for i in range(7):
      oneRowGood()
      driver.swipe(x/2, y/2, x/2, y/2 - goodItem / 3 * 2) # 
      sleep(1)
    driver.swipe(x/2, y/2, x/2, y/2 - goodItem) # 加载更多
    sleep(3)

# 等待启动完成。应该精准判断Activity的状态，还没查资料，偷懒直接sleep!!!
sleep(1)
run()