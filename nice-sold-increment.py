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
desired_caps['appPackage'] = 'com.nice.main'
desired_caps['appActivity'] = 'com.nice.main.activities.MainActivity_'
desired_caps['sessionOverride'] = False

os.system("adb\\adb connect 127.0.0.1:62001")

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
quantity = 1
x = 720
y = 1280
header = 240
offsetTop = 337
goodItem = 442
recordHeight = 88
rows = 0

def back():
  os.system("adb\\adb shell input keyevent 4")

def gotoAllSold():
  try:
    sleep(0.5)
    if ('.shop.record.SkuRecordActivity_' == driver.current_activity):
      beforeSource = None
      isBreak = False # 跳出外层循环
      for i in range(1000):
        if ('.shop.record.SkuRecordActivity_' != driver.current_activity):
          break
        driver.swipe(x/2, y * 2 / 3, x/2, 200)
        currentSource = driver.page_source
        if (currentSource == beforeSource):
          break
        else:
          beforeSource = currentSource

        try:
          if (isBreak):
            break
          dates = driver.find_elements_by_id('com.nice.main:id/tv_deal_time')
          for m in range(len(dates)):
            date = dates[m].get_attribute('text')
            if(date == "2天前"):
              isBreak = True # 跳出外层循环
              break
        except Exception:
          # print('')
          t = None
    back()
    sleep(0.5)
  except Exception:
    print("点击(全部)购买记录 crash")
  finally:
    global quantity
    quantity = quantity + 1

def run():
  skus = []
  file = codecs.open("nice-ids.txt", encoding='UTF-8') 
  for line in file:
    line=line.strip('\r\n')
    skus.append(line)
  file.close()

  
  for a in range(len(skus)):
    print(a + 1)
    sku = skus[a]
    
    cmd = 'adb\\adb shell am start -W -n "com.nice.main/.shop.record.SkuRecordActivity_" --es "goodsId" ' + '"' + sku + '"'
    print(cmd)
    os.system(cmd)
    gotoAllSold()
sleep(2)
try:
  run()
except Exception:
  print("run crash")
finally:
  f = open('nice-rows.txt', 'w')
  f.write(str(rows))
  f.close
  print('[执行结束]====>', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), '<====[执行结束]')