#读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
#加入了我自己的元素：不用输入而是随机读取 使用了延迟函数
import random
import time
n=1
while n<=7:
  x=random.randint(1,50)
  print('*'*x+'   x is %d.'%x)
  n+=1
  time.sleep(1)