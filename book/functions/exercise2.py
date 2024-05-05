foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

# Prints bar since foo is defined as bar in global scope. foo is qux only in function set_foo by functional scope.