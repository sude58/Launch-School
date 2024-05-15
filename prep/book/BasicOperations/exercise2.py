n = 4936

# One place
ones = n % 10
print(f'One place: {ones}')
# Ten Place
ten = n % 100
ten = ten // 10
print(f'Ten place: {ten}')
# Hundreds Place
hundreds = n % 1000
hundreds = hundreds // 100
print(f'Hundreds place: {hundreds}')
# Thousands Place
print(f'Thousands Place: {n // 1000}')