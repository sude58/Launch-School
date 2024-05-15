s = 'launch school tech & talk'
ses = s.split(' ')
new_ses = []
for s in ses:
  s = s.capitalize()
  new_ses.append(s)
print(' '.join(new_ses))