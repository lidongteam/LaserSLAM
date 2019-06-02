#题目：输出 9*9 乘法口诀表
for i in range(1, 10):
	print(' ')
	for j in range(0, i):
		print("{}*{}={}".format(i,j+1,i*(j+1)),end=' ')