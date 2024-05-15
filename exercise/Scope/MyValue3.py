def my_function():
    a = 1

    if True:
        print(a)

my_function() # It will print 1 since a will find its value outside of block scope, which is still in functional scope.