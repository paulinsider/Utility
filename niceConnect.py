#coding=utf-8
from appium import webdriver
import os
from time import sleep

def connect():
  desired_caps = {}
  desired_caps['platformName'] = 'Android'
  desired_caps['platformVersion'] = '4.4.2' # 要跟模拟器版本完全一致
  desired_caps['noReset'] = True
  desired_caps['deviceName'] = '127.0.0.1:62025'
  desired_caps['udid'] = '127.0.0.1:62025'
  desired_caps['appPackage'] = 'com.nice.main'
  desired_caps['appActivity'] = 'com.nice.main.activities.MainActivity_'
  desired_caps['sessionOverride'] = False

  os.system("adb\\adb connect 127.0.0.1:62025")

  driver = webdriver.Remote('http://localhost:4725/wd/hub', desired_caps)
  return driver

def tabShose(driver):
  driver.find_element_by_android_uiautomator('text("好货")').click()
  sleep(1)
  driver.find_element_by_android_uiautomator('text("球鞋")').click()

def back():
  os.system("adb\\adb -s 127.0.0.1:62025 shell input keyevent 4")