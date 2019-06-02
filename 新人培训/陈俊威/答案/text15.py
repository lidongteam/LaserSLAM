#题目15：
#代码：编写input()和output()函数输入，输出5个学生的数据记录。
if __name__=='__main__':
	student=[]
	n=5
	for i in range(5):
		student.append(['','',[]])
	def input(stu):
		for i in range(n):
			stu[i][0]=input('input student name:\n')
			stu[i][1]=input('input student num:\n')
	def output(stu):
		for i in range(n):
			for j in range(2):
				print(stu[i][j])
	if __name__ == '__main__':
		input(student)
		output(student)