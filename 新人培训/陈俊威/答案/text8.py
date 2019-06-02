			
#题目8：学习使用auto定义变量的用法。
if __name__=='__main__':
		num = 2
	def autofunc():
		num = 5
		print ('internal block num=',num)
		num += 1
	for i in range(1,5):
		print ('the num=',num)
		num += 1
		autofunc()