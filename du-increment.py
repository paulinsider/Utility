#coding=utf-8
from appium import webdriver
from time import sleep
import time
import re
import os
import sys

import datetime

print('[执行开始]====>', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), "<====[执行开始]")

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2' # 要跟模拟器版本完全一致
desired_caps['noReset'] = True
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.shizhuang.duapp'
desired_caps['appActivity'] = 'com.shine.ui.home.SplashActivity'

os.system("adb\\adb connect 127.0.0.1:62001")

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
quantity = 1
x = 720
y = 1280
header = 146
goodItem = 354
recordHeight = 88

def tabShose():
  driver.find_element_by_android_uiautomator('text("球鞋")').click()

def tap1():
  try:
    driver.tap([(x / 4,     header + goodItem/2)])
  except Exception:
    print("tap 1 Exception")
def tap2():
  try:
    driver.tap([(x / 4 * 3, header + goodItem/2)])
  except Exception:
    print("tap 2 Exception")
def tap3():
  driver.tap([(x / 4,     header + goodItem/2 * 3)])
def tap4():
  driver.tap([(x / 4 * 3, goodItem/2 * 3)])
def tap5():
  driver.tap([(x / 4,     header + goodItem/2 * 5)])
def tap6():
  driver.tap([(x / 4 * 3, header + goodItem/2 * 5)])

taps = [tap1, tap2, tap3, tap4, tap5, tap6]

def swipePage():
  driver.swipe(x/2, 1000, x/2, header, 500)

def back():
  os.system("adb\\adb shell input keyevent 4")

def visiblityAllSold():
  # 向上滑动，购买记录元素可视
  driver.swipe(360, 700, 360, 246, 500)
  sleep(1)

def soldNum():
  visiblityAllSold()
  global quantity
  soldNum = 10
  try:
    soldNumTxt = driver.find_element_by_id('com.shizhuang.duapp:id/tv_sold_num').get_attribute('text')
    print(quantity, soldNumTxt)
    # 购买记录总条数
    soldNum = re.findall('\d+',soldNumTxt)[0]
  except Exception:
    print(quantity, "获取(全部)购买记录 crash")
  finally:
    return int(soldNum)

onePs = None
twoPs = None

def gotoAllSold(i):
  global onePs
  global twoPs
  if (i == 0):
    cPs = driver.page_source
    if (cPs == onePs):
      return
    else:
      onePs = cPs
  else:
    cPs = driver.page_source
    if (cPs == twoPs):
      return
    else:
      twoPs = cPs
  visiblityAllSold()
  try:
    allEl = driver.find_element_by_id('com.shizhuang.duapp:id/tv_sold_all')
    allEl.click()
    sleep(1) # 进入记录页等待数据加载完成
    if ('com.shine.ui.mall.SoldListActivity' == driver.current_activity):
      beforeSource = None
      for i in range(100):
        if ('com.shine.ui.mall.SoldListActivity' != driver.current_activity):
          break
        driver.swipe(x/2, y - recordHeight, x/2, y - 11 * recordHeight) # 每页20条数据
        
        currentSource = driver.page_source
        if (currentSource == beforeSource):
          break
        else:
          beforeSource = currentSource

        try:
          dates = driver.find_elements_by_id('com.shizhuang.duapp:id/tv_date')
          date = dates[-1].get_attribute('text')
          
          if(date == "2天前"):
            break
        except Exception:
          # print('')
          t = None
    back()
    if ('com.shine.ui.trend.TrendAddNewActivity' == driver.current_activity):
      try:
        driver.find_element_by_android_uiautomator('text("确定")').click()
      except Exception:
        print("click sure back")
  except Exception:
    print("点击(全部)购买记录 crash")
  finally:
    global quantity
    quantity = quantity + 1

def oneRowGood():
  for i in range(2):
    if ('com.shine.ui.home.HomeActivity' != driver.current_activity):
      return
    taps[i]() # 点击列表进入详情
    sleep(1)
    if (len(sys.argv) >= 3):
      gotoAllSold(i) # 去购买记录
      sleep(1)
    currentActivity = driver.current_activity
    if ('com.shine.ui.mall.ProductDetailActivity' == currentActivity):
      back()
    sleep(1)

def run():
  tabShose()
  sleep(1)
  if (len(sys.argv) >= 2):
    for t in range(int(sys.argv[1])):
      try:
        driver.swipe(x/2, y/2, x/2, y/2 - goodItem) # 
      except Exception:
        print("swipe history crash")
  while(True):
    
    for i in range(7):
      oneRowGood()
      try:
        driver.swipe(x/2, y/2, x/2, y/2 - goodItem * 9 / 10) # 
      except Exception:
        print("swipe crash")
      sleep(1)
    # driver.swipe(x/2, y/2, x/2, y/2 - goodItem, 500) # 加载更多
    sleep(1)

# 等待启动完成。应该精准判断Activity的状态，还没查资料，偷懒直接sleep!!!
sleep(5)
try:
  run()
except Exception:
  print("run crash")
finally:
  print('[执行结束]====>', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), '<====[执行结束]')
