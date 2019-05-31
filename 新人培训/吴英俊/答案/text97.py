#从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止
filename=input('Please enter the filename:')
fp=open('filename','w')
ch=input('Please enter the string:')
while ch!='#':
  fp.write(ch)
  ch=input('Please enter the string:')
fp=open('filename','r')
print(fp.read())
fp.close()