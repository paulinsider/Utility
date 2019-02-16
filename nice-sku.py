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


def tap1():
  try:
    driver.tap([(x / 4,     goodItem/2)], 500)
  except Exception:
    print("tap 1 Exception")
def tap2():
  try:
    driver.tap([(x / 4 * 3, goodItem/2)], 500)
  except Exception:
    print("tap 2 Exception")

taps = [tap1]


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

onePs = None
twoPs = None
def gotoAllSold(i):
  if ('.shop.detail.ShopSkuDetailActivity_' != driver.current_activity):
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
  try:
    sleep(1)
    allEl = driver.find_element_by_id('com.nice.main:id/tv_all_deal')
    allEl.click()
    sleep(1) # 进入记录页等待数据加载完成
    if ('.shop.record.SkuRecordActivity_' == driver.current_activity):
      beforeSource = None
      for i in range(50):
        if ('.shop.record.SkuRecordActivity_' != driver.current_activity):
          break
        driver.swipe(x/2, y * 2 / 3, x/2, 200) # 上拉加载更多
        currentSource = driver.page_source
        if (currentSource == beforeSource):
          break
        else:
          beforeSource = currentSource

        try:
          dates = driver.find_elements_by_id('com.nice.main:id/tv_deal_time')
          date = dates[-1].get_attribute('text')
          dm = strftime = datetime.datetime.strptime(date, "%m月%d日")

          cm = datetime.datetime.now().month
          # strftime2 = datetime.datetime.strptime("2018-12-31", "%Y-%m-%d")
          if(dm > cm):
            break
        except Exception:
          # print('')
          t = None
    niceConnect.back()
  except Exception:
    print("点击(全部)购买记录 crash")
  finally:
    global quantity
    quantity = quantity + 1



def oneRowGood():
  global rows
  rows = rows + 1
    
  tap1()
  sleep(1)
  if (len(sys.argv) >= 2):
    gotoAllSold(1)
    sleep(1)
  currentActivity = driver.current_activity
  if ('.shop.detail.ShopSkuDetailActivity_' == currentActivity):
    niceConnect.back()
  sleep(1)

def run():
  skus = []
  file = codecs.open("nice-sku.txt", encoding='UTF-8') 
  for line in file:
    line=line.strip('\r\n')
    skus.append(line)
  file.close()

  niceConnect.tabShose(driver)
  driver.find_element_by_id('com.nice.main:id/tv_search').click()
  for a in range(len(skus)):
    sku = skus[a]
    try: 
      driver.find_element_by_id('com.nice.main:id/search_txt').send_keys(sku)
    except Exception:
      # adf
    sleep(1)
    oneRowGood()
    sleep(1)
    try:
      driver.find_element_by_id('com.nice.main:id/search_txt').clear()
    except Exception
      # 
    # driver.find_element_by_id('com.nice.main:id/tv_search')
    # for i in range(7):
    #   oneRowGood()
    #   try:
    #     driver.swipe(x/2, y/2, x/2, y/2 - goodItem * 9 / 10) # 
    #   except Exception:
    #     print("swipe crash")

    #   sleep(1)
    # # driver.swipe(x/2, y/2, x/2, y/2 - goodItem) # 加载更多
    # sleep(1)
# run()
sleep(1)
try:
  run()
except Exception:
  print("run crash")
finally:
  f = open('nice-rows.txt', 'w')
  f.write(str(rows))
  f.close
  print('[执行结束]====>', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), '<====[执行结束]')