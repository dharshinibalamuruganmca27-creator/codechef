import numpy as np 
N,M = map(int, input().split())
a = np.array([input().split() for _ in range(N)], int)
b = np.array([input().split() for _ in range(N)], int)

print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.floor_divide(a,b))
print(np.mod(a,b))
print(np.power(a,b).astype(int))
