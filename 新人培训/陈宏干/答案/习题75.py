#题目：放松一下，算一道简单的题目
for i in range(5):
  n = 0
  if i != 1: 
    n += 1
  if i == 3:
    n += 1
  if i == 4: 
    n += 1
  if i != 4: 
    n += 1
  if n == 3: 
    print (64 + i)