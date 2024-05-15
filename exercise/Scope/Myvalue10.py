b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b) # It will print [10, 2, 3] since b will be mutated by function.