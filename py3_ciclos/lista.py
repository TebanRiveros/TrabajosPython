def llene_lista(A,B):
  n=len(A)//2
  C=[]
  for i in range(n):
    d=(A[i+1])**2
    e=d*B[2*i]
    f=e+B[n+i]
    C.append(f)
  return C

A=[4,6,8,2]
B=[2,1,0,-1]

print(llene_lista(A,B))