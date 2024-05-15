a = 7

def my_function(b):
    b += 10

my_function(a)
print(a) # It will print 7 since integer is immutable. So while b is updated to value 17, a will remain unchanged. 