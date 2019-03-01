#coding=utf-8
from appium import webdriver
from time import sleep
import time
import re
import os
import sys

import datetime

import duConnect

print('[执行开始]====>', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), "<====[执行开始]")

driver = duConnect.connect()

quantity = 1
x = 720
y = 1280
header = 146
goodItem = 354
recordHeight = 88

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
      for i in range(500):
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
          
          if(date == "4天前" or date == "5天前" or date == "6天前"):
            break
          
          strftime = datetime.datetime.strptime(date, "%Y.%m.%d")
          strftime2 = datetime.datetime.strptime("2019-2-25", "%Y-%m-%d")
          if(strftime <= strftime2):
            break
        
          try:
            strftime = datetime.datetime.strptime(date, "%Y.%m.%d")
          except Exception:
            strftime = datetime.datetime.strptime('2019.' + date, "%Y.%m.%d")
          strftime2 = datetime.datetime.strptime("2019.2.25", "%Y.%m.%d")
          if(strftime <= strftime2):
            break
          
        except Exception:
          # print('')
          t = None
    duConnect.back()
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
rows = 0
def oneRowGood():
  global rows
  
  for i in range(2):
    if ('com.shine.ui.home.HomeActivity' != driver.current_activity):
      return
    taps[i]() # 点击列表进入详情
    rows = rows + 1
    print(rows)
    sleep(1)
    if (len(sys.argv) >= 3):
      gotoAllSold(i) # 去购买记录
      sleep(1)
    currentActivity = driver.current_activity
    if ('com.shine.ui.mall.ProductDetailActivity' == currentActivity):
      duConnect.back()
    sleep(1)

def run():
  duConnect.tabShose(driver)
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
