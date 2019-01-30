#coding=utf-8
from appium import webdriver
from time import sleep
import time
import re
import os
import sys

print('[执行开始 even]====>', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), "<====[执行开始 even]")

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2' # 要跟模拟器版本完全一致
desired_caps['noReset'] = True
desired_caps['deviceName'] = '127.0.0.1:62001'
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
  driver.tap([(x / 4,     header + goodItem/2)])
def tap2():
  driver.tap([(x / 4 * 3, header + goodItem/2)])
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
def gotoAllSold():
  sn = soldNum() # 获取购买数量
  pageSize = 20
  pageVisibilite = 12
  try:
    allEl = driver.find_element_by_id('com.shizhuang.duapp:id/tv_sold_all')
    allEl.click()
    count = int(sn / pageVisibilite) + 1
    # if(count > 1):
    #   count = 1
    sleep(1) # 进入记录页等待数据加载完成
    for i in range(count):
      # for j in range(pageSize):
      driver.swipe(x/2, y - recordHeight, x/2, y - 11 * recordHeight) # 每页20条数据
      driver.swipe(x/2, y - recordHeight, x/2, y - 11 * recordHeight) # 每页20条数据
      
      driver.swipe(x/2, y/2, x/2, y/2 - recordHeight * 2) # 上拉加载更多
      sleep(1)
    back()
  except Exception:
    print("点击(全部)购买记录 crash")
  finally:
    global quantity
    quantity = quantity + 1

def oneRowGood():
  # for i in range(2):
  tap1() # 点击列表进入详情
  sleep(1)
  if (len(sys.argv) >= 2):
    gotoAllSold() # 去购买记录
    sleep(1)
  back() # 返回列表
  sleep(1)

def run():
  tabShose()
  sleep(1)

  while(True):
    
    for i in range(7):
      oneRowGood()
      driver.swipe(x/2, y/2, x/2, y/2 - goodItem / 3 * 2, 500) # 
      sleep(0.5)
    driver.swipe(x/2, y/2, x/2, y/2 - goodItem, 500) # 加载更多
    sleep(1)

# 等待启动完成。应该精准判断Activity的状态，还没查资料，偷懒直接sleep!!!
sleep(5)
try:
  run()
finally:
  print('[执行结束 even]====>', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), '<====[执行结束even]')