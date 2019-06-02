#题目13：输入3个数a,b,c，按大小顺序输出。
#代码：
	    if __name__=='__main__':
			a=int(input('a='))
			b = int(input('b='))
			c = int(input('c='))
			def swap(i,j):
				return j,i
			if (a>b):
				a,b=swap(a,b)
			if (a>c):
				a,c= swap(a,c)
			if (b > c):
				b,c=swap(b,c)
			print(a,b,c)