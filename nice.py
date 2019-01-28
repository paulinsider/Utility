#coding=utf-8
from appium import webdriver
from time import sleep
import time
import re
import os
import sys

print('[执行开始]====>', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), "<====[执行开始]")

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2' # 要跟模拟器版本完全一致
desired_caps['noReset'] = True
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.nice.main'
desired_caps['appActivity'] = 'com.nice.main.activities.MainActivity_'

os.system("adb\\adb connect 127.0.0.1:62001")

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
quantity = 1
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
  sleep(1)

def soldNum():
  visiblityAllSold()
  global quantity
  soldNum = 10
  try:
    snEl = driver.find_element_by_id('com.nice.main:id/tv_title')
    soldNumTxt = snEl.get_attribute('text')
    print(quantity, soldNumTxt)
    # 购买记录总条数
    soldNum = re.findall('\d+',soldNumTxt)[0]
  except Exception:
    print(quantity, "获取(全部)购买记录 crash")
  finally:
    return soldNum
def gotoAllSold():
  sn = soldNum()
  try:
    driver.swipe(x/2, y - 200 - y * 2 / 3, x/2, y - 200, 500)
    sleep(1)
    allEl = driver.find_element_by_id('com.nice.main:id/tv_all_deal')
    allEl.click()
    sleep(1) # 进入记录页等待数据加载完成
    for i in range(sn):
      driver.swipe(x/2, y * 2 / 3, x/2, 200 , 500) # 上拉加载更多
      sleep(1)
    back()
  except Exception:
    print("点击(全部)购买记录 crash")
  finally:
    global quantity
    quantity = quantity + 1



def oneRowGood():
  for i in range(2):
    taps[i]()
    sleep(1)
    if (len(sys.argv) >= 2):
      gotoAllSold()
      sleep(1)
    currentActivity = driver.current_activity
    if ('.shop.detail.ShopSkuDetailActivity_' == currentActivity):
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
    # driver.swipe(x/2, y/2, x/2, y/2 - goodItem) # 加载更多
    sleep(1)

sleep(1)
try:
  run()
finally:
  print('[执行结束]====>', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), '<====[执行结束]')