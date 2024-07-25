import numpy as np
import timeit
a = np.array([4, 5, 1])
vectorized_product = np.prod(a)
print("Vectorized Product:", vectorized_product)
print("Time taken by vectorized product:", end=" ")
vectorized_time = timeit.timeit('np.prod(a)', globals=globals(), number=10000)
print(vectorized_time)
total = 1
for item in a:
    total *= item
iterative_product = total
print("Iterative Product:", iterative_product)
print("Time taken by iterative multiplication:", end=" ")
iterative_time = timeit.timeit('''
total = 1
for item in a:
    total *= item
''', globals=globals(), number=10000)
print(iterative_time)
