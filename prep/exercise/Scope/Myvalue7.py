a = 1

def my_function():
    global a
    a = 2

my_function()
print(a) # It will print 2 since global statement makes a in function global variable. So change in a in the function affects the global variable.