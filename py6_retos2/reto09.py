inicial=int(input("numero inicial"))
final=int(input("numero final"))
intervalo=int(input("intervalo"))
total=0
for i in range(inicial, final, intervalo):
  total=total+i
  print(i)

print("La suma es: ",total)