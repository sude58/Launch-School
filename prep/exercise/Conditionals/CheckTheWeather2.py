weather = 'sunny'

match weather:
  case 'sunny':
    print('It\'s a beautiful day')
  case 'rainy':
    print('Grab your umbrella.')
  case 'snowy':
    print('Wear your winter clothes.')
  case _:
    print('Let\'s stay inside')