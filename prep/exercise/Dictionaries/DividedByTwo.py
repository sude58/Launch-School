numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

values = list(numbers.values())
half_numbers = []
for value in values:
  value /= 2
  value = int(value)
  half_numbers.append(value)
print(half_numbers)