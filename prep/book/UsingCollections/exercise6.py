print('abc-def'.isalpha()) # false
print('abc_def'.isalpha()) # false
print('abc def'.isalpha()) # false
print('abc def'.isalpha() and
      'abc def'.isspace()) # false
print('abc def'.isalpha() or
      'abc def'.isspace()) # false
print('abcdef'.isalpha()) # True
print('31415'.isdigit()) # True
print('-31415'.isdigit()) # False
print('31_415'.isdigit()) # False
print('3.1415'.isdigit()) # False
print(''.isspace()) # False 
# Empty string return false to most isXXXX string method.