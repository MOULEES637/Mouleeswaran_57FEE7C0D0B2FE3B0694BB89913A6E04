def factorial(x):
  """This is arecursibe function to find thefactorial of an integer"""
  if x==1:
    return 1
  else:
    return(x*factorial(x-1))
num=7
result=factorial(num)
print("The factorial of",num,"is",result)
