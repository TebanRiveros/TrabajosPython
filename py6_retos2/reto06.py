import random

numero=random.randrange(1, 120)

if (numero<10):
  print(numero, " es menor a 10")
elif (numero>10 and numero<50):
  print(numero, " esta entre 10 y 50")
elif (numero>50 and numero<100):
  print(numero, " esta entre 50 y 100")
elif (numero>10):
  print(numero," es mayor a 100")