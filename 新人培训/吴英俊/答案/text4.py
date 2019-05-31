# 输入某年某月某日，判断这一天是这一年的第几天？
year=int(input('Please enter year:'))
month=int(input('Please enter month between 1 and 12:'))
day=int(input('Please enter day between 1 and 31:'))
Month=[31,28,31,30,31,30,31,31,30,31,30,31]
if month==1:
  sum=day
else:
  sum=0
  for i in range(month-1):
    sum += Month[i]
  sum+=day
  if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    sum += 1
print('This day is %dth day.' %sum)