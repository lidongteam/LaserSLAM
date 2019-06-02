#题目：求100之内的素数。
for num in range(1,101):
    if num > 1:
        for i in range(2,100):
            if(num%i==0):
                break
            else:
                print(num)