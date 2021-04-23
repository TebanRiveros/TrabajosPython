def bisiesto(año):
  if año%4==0:
    if año%100!=0:
      print(f'{año} es bisiesto')
  else:
    if año%400==0:
      print(f'{año} es bisiesto')
    print(f'{año} no es bisiesto')

bisiesto(2012)