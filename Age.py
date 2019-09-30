print('How old are you?')
age = int(input())

if age == 18:
  print('Congrats, you are 18!')
  
if age < 18:
  dif = 18 - age
  print('you will be 18 in', dif)
else:
  dif = age -18
  print('you were 18', dif, 'years ago')
