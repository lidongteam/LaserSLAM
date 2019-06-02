#题目20：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
#代码：
if __name__ == '__main__':
	a=int(input('输入一个数字：'))
	b=1
	c=9
	num=1
	while(b!=0):
		if(c%a==0):
			b=0
		else:
			c=c*10+9
			num=num+1