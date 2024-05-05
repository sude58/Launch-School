stuff = ('hello', 'world', 'byte', 'now')

stuff = ('hello', 'world', 'goodbye', 'now')

print(stuff)

# Better answer
'''
stuff = list(stuff)
stuff[2] = 'goodbye'
stuff = tuple(stuff)
'''