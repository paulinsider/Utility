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

def gotoAllSold():
  try:
    sleep(0.5)
    if ('.shop.record.SkuRecordActivity_' == driver.current_activity):
      beforeSource = None
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
          dates = driver.find_elements_by_id('com.nice.main:id/tv_deal_time')
          date = dates[-1].get_attribute('text')
          strftime = None
          try:
            strftime = datetime.datetime.strptime(date, "%Y年%m月%d日")
          except Exception:
            strftime = datetime.datetime.strptime('2019年' + date, "%Y年%m月%d日")
          
          beforeDate = "2018-12-31"
          if (len(sys.argv) >= 2):
            beforeDate = sys.argv[1]
          strftime2 = datetime.datetime.strptime(beforeDate, "%Y-%m-%d")
          if(strftime < strftime2):
            break
        except Exception:
          # print('')
          t = None
    niceConnect.back()
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