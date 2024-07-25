import numpy as np
import random
array = np.random.randint(16,size=(4,4)) 
print("Input Array: \n",array)
print("Smallest number in x axis:", np.min(array,axis=1))
print("Smallest number in y axis:",np.min(array,axis=0))