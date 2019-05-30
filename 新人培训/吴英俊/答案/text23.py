'''打印出如下图案（菱形）:   
   *
  ***
 *****
*******
 *****
  ***
   *
'''
#本题可以直接写代码，如果在不知道输入图形大小的情况下，可以自己编写一个函数，分成奇偶两种
from sys import stdout
for i in range(4):
  for j in range(3-i):
    stdout.write(' ')
  for k in range(2*i+1):
    stdout.write('*')
  print('\n')
for i in range(3):
  for j in range(i+1):
    stdout.write(' ')
  for k in range(5-2*i):
    stdout.write('*')
  print('\n')