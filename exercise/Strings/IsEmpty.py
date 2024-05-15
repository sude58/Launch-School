def is_empty(string):
  if len(string):
    return False
  else:
    return True

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True