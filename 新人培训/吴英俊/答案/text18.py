#求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
from functools import reduce
An=[]
a=int(input('Please enter a digit between 0 and 9:'))
n=int(input('Please enter times:'))
if (a<0 or a>=10):
  print('Error:please enter a correct digit')
else:
  Sn=0
  for i in range(n):
    Sn=Sn*10+a
    An.append(Sn)
  Sn =reduce(lambda x,y:x+y,An)
print('sum=%d' %Sn) 

