import numpy as np
import random
array=np.random.randint(16,size=(4,4))
print ("input array: \n",array)
print ("largest number in x axis:", np.max(array,axis=1))
print ("largest number in y axis:", np.max(array,axis=0))
