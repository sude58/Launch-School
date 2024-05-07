dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

# It will print [1, 42, 3] since dict2 is a shallow copy of dict1. Since dict1[a] is a neseted collection, dict2 will share its reference with dict1. So dict2 will change its value too when changing value in dict1.