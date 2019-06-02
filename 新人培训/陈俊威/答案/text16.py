#题目16：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，
#调用函数1/1+1/3+...+1/n
#代码：
if __name__=='__main__':
	def even(n):
		i = 0
		sum = 0
		for i in range(2, n + 1, 2):
			sum += 1 / i
		return sum


	def odd(n):
		sum = 0
		for i in range(1, n + 1, 2):
			sum += 1 / i
		return sum


	def sum(f, n):
		s = f(n)
		return s


	if __name__ == '__main__':
		n = int(input('input a number:\n'))
		if n % 2 == 0:
			sum = sum(even, n)
		else:
			sum = sum(odd, n)
		print(sum)
