dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])

# Ir will print 'The Life of Brain' since dict2 is a shallow copy of dict1. Then dict2 is a new object with separate reference sine dict1 is not nested.