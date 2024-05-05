def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# name: mutiply, parameters: left, right, defined in line 1-2 and invoked in line 9
# name: get_num, parameters: prompt, defined in line 4-5 and invoked in line 7,8
# name: float, built-in function invoked in line 5
# name: input, built-in function invoked in line 5
# name: print, built-in function invoked in line 10