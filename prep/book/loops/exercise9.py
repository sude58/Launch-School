def factorial(n):
  answer = 1
  for x in range(2, n + 1):
    answer *= x
  return answer

# def factorial_while(n):
#   i = 1
#   while i < n:
#     answer *= i
#     i += 1
#   return answer

print(factorial(1))   # 1
print(factorial(2))   # 2
print(factorial(3))   # 6
print(factorial(4))   # 24
print(factorial(5))   # 120
print(factorial(6))   # 720
print(factorial(7))   # 5040
print(factorial(8))   # 40320
print(factorial(25))  # 15511210043330985984000000