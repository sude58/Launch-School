def set_foo():
    foo = 'bar'

set_foo()
print(foo)

# Raise name error since foo is not defined in a global scope. foo is only in functional scope, which cannot be accessed globally.