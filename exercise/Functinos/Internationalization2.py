def greet(code):
  match code:
    case 'en':
      return 'Hi!'
    case 'fr':
      return 'Salut!'
    case 'pt':
      return 'Olá!'
    case 'de':
      return 'Hallo!'
    case 'sv':
      return 'Hej!'
    case 'af':
      return 'Haai!'
    case _:
      return 'Not availiable'

def extract_language(code):
  return code[:2]

def extract_region(code):
  return code[3:5]

def local_greet(text):
  code = extract_language(text)
  if code == 'en':
    match extract_region(text):
      case 'US':
        return 'Hey!'
      case 'GB':
        return 'Hello!'
      case 'AU':
        return 'Howdy!'
  else:
    return greet(code)

print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!