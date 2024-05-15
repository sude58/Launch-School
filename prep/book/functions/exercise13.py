def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)
# Will raise an error since third comes after default argument and not default argument.