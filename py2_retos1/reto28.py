print(f'\nTabla del 1\n')
for i in range(1,11):
  for j in range (1,11):
    x=i*j
    print(f'{i} * {j} = {x}')
    if j == 10 and i!=10:
      print(f'\nTabla del {i+1}\n')