def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))

# function name: say
# method name: upper, lower
# built-in: input, print, max