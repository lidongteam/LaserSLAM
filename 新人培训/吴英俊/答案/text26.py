def factorial(n):
  #if not isinstance(n,(int)):
    #raise TypeError('bad operand type')
  sum=0
  if n==0:
    sum=1
  else:
    sum = n * factorial(n-1)
  return sum
x=int(input('Please enter x:'))
print(factorial(x))