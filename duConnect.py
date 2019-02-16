#coding=utf-8
from appium import webdriver
import os
from time import sleep

def connect():
  desired_caps = {}
  desired_caps['platformName'] = 'Android'
  desired_caps['platformVersion'] = '4.4.2' # 要跟模拟器版本完全一致
  desired_caps['noReset'] = True
  desired_caps['deviceName'] = '127.0.0.1:62001'
  desired_caps['udid'] = '127.0.0.1:62001'
  desired_caps['appPackage'] = 'com.shizhuang.duapp'
  desired_caps['appActivity'] = 'com.shine.ui.home.SplashActivity'

  os.system("adb\\adb connect 127.0.0.1:62001")

  driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
  return driver

def tabShose(driver):
  try:
    driver.find_element_by_android_uiautomator('text("购买")').click()
  except Exception:
    print("tap 购买 Exception")
  try:
    driver.find_element_by_android_uiautomator('text("球鞋")').click()
  except Exception:
    print("tap 球鞋 Exception")

def back():
  os.system("adb\\adb -s 127.0.0.1:62001 shell input keyevent 4")