#题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
n =int(input('n= '))
a =int(input('a= '))
num,sum =0,0
for i in range(1,n+1):
    num =num*10+a
    print(num)
    sum=sum+num
    
print('和为%d'%sum)