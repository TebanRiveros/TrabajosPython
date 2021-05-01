A=['almeja','mantequilla','elefante','sol','pasta']

solo_a=[A[x]  for x in range(len(A)) if A[x][-1]=='a' ]

print(solo_a)