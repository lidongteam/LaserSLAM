#题目7：求100之内的素数。
if __name__ == '__main__':
	for num in range(2,101):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)