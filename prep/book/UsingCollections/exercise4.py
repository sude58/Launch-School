pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

# Part 1
print(pets['Dog'])

# Part 2
key = 'Lizard'
if key not in pets.keys():
  print(None)

# Part 3
if key not in pets.keys():
  print('<silence>')