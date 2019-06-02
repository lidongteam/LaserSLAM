#题目10：输出一个随机数。
	# （1）随机输出一个实数
	if __name__=='__main__':
	   import random
		 a=random.uniform(1,10)
		 print(a)
	  #（2）随机输出一个整数
	    import random
	    a=random.randint(1,10)
	    print(a)
	  #（3）随机输出一个字符
		import random
		a=random.choice('随机选取一个字符')
		print(a)