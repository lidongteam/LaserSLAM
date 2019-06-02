#题目6：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
if __name__=='__main__':
		letter=input('please input first letter:')
		if letter=='M':
			print('Monday')
		elif letter=='T':
			print('pleasr input second letter:')
			letter=input()
			if letter=='u':
				print('Tuesday')
			elif letter=='h':
				print('Thursday')
			else:
				print('error')
		elif letter == 'W':
			print('Wednesday')
		elif letter == 'F':
			print ('Friday')
		elif letter=='S':
			print('please input second letter:')
			letter=input()
			if letter=='a':
				print('Saturday')
			elif letter=='u':
				print('Sunday')
			else:
				print('error')
		else:
			print('error')