def starts_with(s, substring):
  return s[0:len(substring)] == substring

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True