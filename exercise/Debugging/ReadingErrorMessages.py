def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

# find_first_nonzero_among(0, 0, 1, 0, 2, 0) # TypeError: find_first_nonzero_among() takes 1 positional argument but 6 were given. Functions took too many arguments (more arguments than its parameters)
find_first_nonzero_among(1) # TypeError: 'int' object is not iterable 
# Function's argument has to be iterable since function takes a loop for its argument. Since it isn't it made error.