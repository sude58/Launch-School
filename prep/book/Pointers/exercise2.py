set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)

# It will print a set with elements 42, 'Monty Python', ('a', 'b', 'c'), range(5,10)