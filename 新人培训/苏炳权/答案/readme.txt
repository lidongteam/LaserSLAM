第一题
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print i,j,k
第二题
斐波那契数列
n = raw_input('请输入斐波那契数列的第n个:')
det fib(n):
	if n==1 or n==2:
	    return 1
	else:
	    return fib(n-1)+fib(n-2)
print fib(n)
第三题	
古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
假如兔子都不死，问每个月的兔子总数为多少？
det sum(i):
    for i in range(1,101):
	    if i ==1 or i ==2:
		    return 1
		else:
            sum = sum(i-1)+sum(i-2)
            print sum 			
第四题
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
import string
s = raw_input('请输入一个字符串:\n')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print 'char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others)
第五题
猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
i = 1
for day in range(1,10):
    sum = (i + 1) * 2
    i = sum
print sum
第六题
利用递归方法求5!
def sum(n):
    sum = 0
    if n == 1:
        return 1
    else:
        sum = n * sum(n - 1)
    return sum
 
print sum(5)
第七题
请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母
etter = raw_input("请输入:")
if letter == 'S':
    print ('请输入第二个字母:')
    letter = raw_input("请输入:")
    if letter == 'a':
        print ('Saturday')
    elif letter  == 'u':
        print ('Sunday')
    else:
        print ('error')
    
elif letter == 'F':
    print ('Friday')
    
elif letter == 'M':
    print ('Monday')
    
elif letter == 'T':
    print ('请输入第二个字母')
    letter = raw_input("请输入:")
 
    if letter  == 'u':
        print ('Tuesday')
    elif letter  == 'h':
        print ('Thursday')
    else:
        print ('error')
        
elif letter == 'W':
    print ('Wednesday')
else:
    print ('error')
第八题
求100之内的素数。
for i in range(1,101):
    if i > 1:
        for i in range(1,i):
            if (i % j) == 0:
                break
        else:
            print(i)
第九题
统计 1 到 100 之和
sum = 0
for i in range(1,101):
    sum += i
print 'The sum is %d' % sum
第十题
求输入数字的平方，如果平方运算后小于 50 则退出
while 1>0:
    i = int(raw_input('请输入一个数字:'))
	num i*i
	if num < 50:
	    break
	print 'num = %d' % num	
第十一题
查找字符串
sStr1 = 'abcdefg'
sStr2 = 'cde'
print sStr1.find(sStr2)
第十二题
输入3个数a,b,c，按大小顺序输出
    n1 = int(raw_input('n1 = :\n'))
    n2 = int(raw_input('n2 = :\n'))
    n3 = int(raw_input('n3 = :\n'))
 
    def swap(b1,b2):
        return b2,b1
 
    if n1 > n2 : 
	    n1,n2 = swap(n1,n2)
    if n1 > n3 : 
	    n1,n3 = swap(n1,n3)
    if n2 > n3 :
     	n2,n3 = swap(n2,n3)
 
    print n1,n2,n3
第十三题
创建一个列表
ptr = []
    for i in range(5):
        num = int(raw_input('请输入一个数字:\n'))
        ptr.append(num)
    print ptr
第十四题
编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
if __name__ == '__main__':
    n = int(raw_input('请输入一个数字:\n'))
	sum = 0
	det sum(n)
	    sum = 0
		if n == 2 or n == 1:
		    return 1/n
		sum = sum+sum(n-2)
		return sum+1/n
第十五题
输入一个奇数，然后判断最少几个 9 除于该数的结果为整数
if __name__ == '__main__':
    num = int(raw_input('请输入一个数字:\n'))
    i = 1
    b = 1
    m = 9
    sum = 9
    while i != 0:
        if sum % num == 0:
            i = 0
        else:
            m *= 10
            sum += m
            b += 1
    print '%d 个 9 可被 %d 整除 : %d' % (b,num,sum)
    k = sum / num
    print '%d / %d = %d' % (sum,num,k)
第十六题
两个字符串连接
if __name__ == '__main__':
    a = "abc"
    b = "def"
    c = a + b
    print c
第十七题
时间函数
if __name__ == '__main__':
    import time
    start = time.time()
    for i in range(300):
        print i
    end = time.time()
    print end - start
第十八题
列表转换为质点
i = ['a', 'd']
j = [1, 2]
print dict([i,j])
第十九题
求一个3*3矩阵主对角线元素之和。
f __name__ == '__main__':
    a = []
    sum = 0
    for i in range(0,3):
        a.append([])
        for j in range(3):
            a[i].append(int(raw_input("请输入:\n")))
    for i in range(0,3):
        sum += a[i][i]
    print sum
第二十题
打印杨辉三角
if __name__ == '__main__':
    a = []
    for i in range(10):
        a.append([])
        for j in range(10):
            a[i].append(0)
    for i in range(10):
        a[i][0] = 1
        a[i][i] = 1
    for i in range(2,10):
        for j in range(1,i):
            a[i][j] = a[i - 1][j-1] + a[i - 1][j]
	print a		


