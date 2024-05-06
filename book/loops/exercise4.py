my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index < len(my_list):
  x = my_list[index]
  if x % 2 == 0:
    print(x)
  index += 1

for x in my_list:
  if x % 2 == 1:
    print(x)