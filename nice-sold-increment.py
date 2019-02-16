#coding=utf-8
from appium import webdriver
from time import sleep
import time
import re
import os
import sys

import datetime
import codecs

import niceConnect

print('[执行开始]====>', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), "<====[执行开始]")

driver = niceConnect.connect()

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
            if(date == "2天前" or date == "3天前" or date == "2天前" or date == "4天前" or date == "5天前" or date == "6天前"):
              isBreak = True # 跳出外层循环
              break
          date = dates[-1].get_attribute('text')
          strftime = datetime.datetime.strptime(date, "%Y.%m.%d")
          strftime2 = datetime.datetime.strptime("2019-2-10", "%Y-%m-%d")
          if(strftime < strftime2):
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