destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(element, sequence):
  for location in sequence:
    if element == location:
      return True
  return False

print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # False
