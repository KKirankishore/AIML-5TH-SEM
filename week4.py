import numpy as n
import timeit
print(n.sum(n.arange(4)))
print("Time taken to vectorized sum:")
timeit,n.sum(n.arange(4))
t=0
for i in range(0,4):
 t+=i
a=t
print("\n"+str(a))
print("Time Taken by iterative sum:",end="")
 
