def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()
# function first takes a list of keys of dictionary. Then it returns sorted list based on the dictionary key. Then it takes second value, which is at index 1 and second in lexical order, and makes it all uppercase.

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))
# It will print CHRIS