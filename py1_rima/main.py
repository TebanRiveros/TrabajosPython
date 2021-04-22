print('hola mundo')

archivo=open('palabras500.csv',encoding='utf-8')

lineas=archivo.readlines()

archivo.close()

'''print(len(lineas))

print(lineas[0])

print(lineas)'''

'''palabra=lineas[0]
silaba=palabra[-3:-1]
print(silaba)'''

def rima(silaba):
  for i in range(500):
    palabra=lineas[i]
    if (palabra[-3:-1])==silaba:
      print(palabra)

rima('an')