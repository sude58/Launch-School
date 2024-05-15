a = 1

def my_function():
    print(a)
    a = 2

my_function() # It will raise an exception. Since a is defined in a local scope, it will try to print local value of a, but it is not defined when print statement is executed. So, it will result error.