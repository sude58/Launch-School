my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

new_dict = {member: len(member) for member in my_set if len(member) % 2 == 1}

print(new_dict)