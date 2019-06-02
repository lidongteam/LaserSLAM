		
#题目4：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分
#以下的用C表示。
	  print('输入成绩：')
	  score=int(input())
	  if score>=90:
		  grade='A'
	  elif score>=60:
		  grade='B'
	  else:
		  grade='C'
	  print(score,'对应等级为：',grade)