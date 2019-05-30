#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
import string
import time
s=input('Please enter a string:')
letters=0
space=0
digit=0
others=0
for i in s :
  if i.isalpha():
    letters+=1
  elif i.isspace():
    space+=1
  elif i.isdigit():
    digit+=1
  else:
    others+=1
print('letters=%d,space=%d,digit=%d,others=%d' %(letters,space,digit,others))

# python3 有一种"fstring"的概念，举个栗子给你看看
print(f"letters={letters},space={space},digit={digit},others={others}")
time.sleep(5)