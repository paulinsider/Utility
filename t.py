import datetime

strftime = datetime.datetime.strptime("12月20日", "%m月%d日")
strftime2 = datetime.datetime.strptime("2018-12-31", "%Y-%m-%d")
print(strftime)
print(strftime2)
import time
time.strftime('%m',time.localtime(time.time()))

print(strftime.month)

print(datetime.datetime.now().month)