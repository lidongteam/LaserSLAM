#题目11：斐波那契数列。
if __name__=='__main__':
		def fib(n):
			a=1
			b=1
			if n==1 or n==2:
				return 1
			else:
				return fib(n-1)+fib(n-2)
		for i in range(1,11):
			print(fib(i))