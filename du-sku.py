#coding=utf-8
from appium import webdriver
from time import sleep
import time
import re
import os
import sys

import datetime
import codecs

print('[执行开始]====>', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), "<====[执行开始]")

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2' # 要跟模拟器版本完全一致
desired_caps['noReset'] = True
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.shizhuang.duapp'
desired_caps['appActivity'] = 'com.shine.ui.home.SplashActivity'
desired_caps["unicodeKeyboard"] = True
desired_caps["resetKeyboard"] = True
# os.system("adb\\adb shell ime set com.sohu.inputmethod.sogou/.SogouIME")
os.system("adb\\adb connect 127.0.0.1:62001")

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
quantity = 1
x = 720
y = 1280
header = 146
goodItem = 354
recordHeight = 88

rows = 0

def tabShose():
  try: 
    driver.find_element_by_android_uiautomator('text("购买")').click()
  except Exception:
    a = 1
  sleep(1)
  try:
    driver.find_element_by_android_uiautomator('text("球鞋")').click()
  except Exception:
    b = 1
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
  if ('com.shine.ui.mall.ProductDetailActivity' != driver.current_activity):
    return
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
          strftime = datetime.datetime.strptime(date, "%Y.%m.%d")
          strftime2 = datetime.datetime.strptime("2018-12-31", "%Y-%m-%d")
          if(strftime < strftime2):
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
  global rows
  rows = rows + 1
  for i in range(1):
    taps[i]() # 点击列表进入详情
    sleep(1)
    if (len(sys.argv) >= 2):
      gotoAllSold(i) # 去购买记录
      sleep(1)
    currentActivity = driver.current_activity
    if ('com.shine.ui.mall.ProductDetailActivity' == currentActivity):
      back()
    sleep(1)

def run():
  tabShose()
  sleep(1)
  skus = []
  # file = codecs.open("du-sku.txt", encoding='UTF-8') 
  # for line in file:
  #   line=line.strip('\r\n')
  #   skus.append(line)
  # file.close()
  with open('du-sku.txt', 'r', encoding='utf-8') as f:
    skus = f.read().splitlines()

  driver.find_element_by_id('com.shizhuang.duapp:id/rl_search').click()
  for a in range(len(skus)):
    sku = skus[a]
    # fil = re.compile(u'[^0-9a-zA-Z.，,。？“”]+', re.UNICODE)
    # sku = fil.sub(' ', sku)
    print(sku)
    try: 

      os.system("adb\\adb shell ime set io.appium.settings/.UnicodeIME")
      sleep(0.5)
      driver.find_element_by_id('com.shizhuang.duapp:id/et_search').send_keys(sku)
      # inputSku = 'adb\\adb shell input text "' + sku + '"'
      # print(inputSku)
      # os.system(inputSku)
      os.system("adb\\adb shell ime set com.sohu.inputmethod.sogou/.SogouIME")
      sleep(0.5)
      driver.find_element_by_id('com.shizhuang.duapp:id/et_search').click()
      os.system("adb\\adb shell input keyevent 66")
    except Exception:
      m = 1
    
    sleep(1)
    oneRowGood()
    sleep(1)
    try:
      driver.find_element_by_id('com.shizhuang.duapp:id/tv_search').click()
      sleep(0.5)
      driver.find_element_by_id('com.shizhuang.duapp:id/et_search').clear()
    except Exception:
      n = 1
    sleep(1)
    
# 等待启动完成。应该精准判断Activity的状态，还没查资料，偷懒直接sleep!!!
sleep(5)
run()
try:
  run()
except Exception:
  print("run crash")
finally:
  f = open('du-rows.txt', 'w')
  f.write(str(rows))
  f.close
  print('[执行结束]====>', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), '<====[执行结束]')
