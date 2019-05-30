#有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
#改一下题目，下面是我自己的一些想法：首先用户输入随机数，输入-1结束，然后排序
#5.30 有一点错误 明日改
L=[]
L1=[]
again=1
while again:
  n=int(input("Please enter a number:"))
  if n==-1:
    again=-1
    break
  else:
    again=1
    L.append(n)
L.sort()
print(L)
x=int(input("Please enter another one number"))
if(x>L[len(L)-1]):
  L.append(x)
  print(L)
else:
  for i in range(len(L)):
    if(x>L[i]):
      a=i+1
      mid=L[i+1]
      L[i+i]=x
      break
  for i in range(a,len(L))  
    L1.append(L[i])
  for i in range(len(L1))
    L.append(len[i])
print(L)