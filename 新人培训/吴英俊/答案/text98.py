#从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
if __name__ == '__main__':
    fp = open('test.txt','w')#w为写入模式
    string = input('please input a string:\n')
    string = string.upper()
    fp.write(string)#write为写入
    fp = open('test.txt','r')#r为只读模式
    print (fp.read())
    fp.close()