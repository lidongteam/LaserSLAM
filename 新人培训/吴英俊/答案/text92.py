#计时
if __name__ == '__main__':
    import time
    start = time.time()
    for i in range(100):
        print (i)
    end = time.time()
    time=end-start
    print ('%.2f'%time)