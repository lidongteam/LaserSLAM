#题目5：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过
#多少米？第10次反弹多高？

	  sum=0
	  height=100
	  for i in range(1,11):
		  sum=sum+height
		  height=height/2
	  print('共经过',sum,'米')
	  print('第十次反弹',height,'米')