def all_caps_long(word):
  if len(word) > 10:
    return word.upper()
  else:
    return word
  
print(all_caps_long('hello world'))
print(all_caps_long('goodbye'))