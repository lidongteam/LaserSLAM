
#题目9：求输入数字的平方，如果平方运算后小于 50 则退出。
if __name__=='__main__':
	def PF(x):
		return x*x
	A=1
	while A:
		i=int(input('输入一个数字：'))
		if PF(i)>=50:
			print('运算结果为：',i*i)
			continue
		else:
			break
	print('输入的数平方运算后小于50，退出')
