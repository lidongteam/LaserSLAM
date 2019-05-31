#一个猜数游戏，判断一个人反应快慢。
import time
import random
play_it=input('Do you want to play it? \'Y\'or \'N\'')
while play_it=='Y':
  i=random.randint(0,101)
  x=int(input('Please enter the number you guess:'))
  times=1
  start=time.time()
  while x!=i: 
    if x<i:
       x=int(input('Please enter a larger number:'))
       times +=1
    if x>i:
       x=int(input('Please enter a lower number:'))
       times +=1
  while x==i:
    end=time.time()
    use_time=end-start
    print('Congratulations!')
    if use_time>30:
      print('you are a little stupid!')
    elif 15<=use_time<=30:
      print ('you are normal!')
    else:
      print ('you are very clever!')
    print('The number is %d,and you only use %d times in %.2f s.'%(i,times,use_time))
    break
  break