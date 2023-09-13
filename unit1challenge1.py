def fact(n):
  if n == 0:
    return 1
  else:
    return n * fact(n - 1)


num = int(input("Enter a number: "))
if num < 0:
  print("Factorial is not for negative numbers.")
else:
  result = fact(num)
  print(f"The factorial of {num} is {result}")