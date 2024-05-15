def number_range(n):
  if n < 0:
    print(f'{n} is less than 0')
  elif n > 100 :
    print(f'{n} is greater than 100')
  elif n > 50:
    print(f'{n} is between 51 and 100')
  else:
    print(f'{n} is between 0 and 50')

number_range(0)     # 0 is between 0 and 50
number_range(25)    # 25 is between 0 and 50
number_range(50)    # 50 is between 0 and 50
number_range(75)    # 75 is between 51 and 100
number_range(100)   # 100 is between 51 and 100
number_range(101)   # 101 is greater than 100
number_range(-1)    # -1 is less than 0
