#暂停一秒输出，并格式化当前时间。
#本题我看了三个函数time.time() time.localtime() time.strftime()
import time
print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
#暂停一秒输出
time.sleep(1)
print (time.strftime('The time is %Y-%m-%d %H:%M:%S',time.localtime(time.time())))