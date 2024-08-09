# Arithmatic operation of numpy

import numpy as np
x=np.array([1,2,8,31,4])
print(np.max(x))
print(np.min(x))
print(np.argmax(x))# return maximum index no
print(np.sin(x))
print(np.cos(x))
print(np.cumsum(x))

                # for 2D array
x=np.array([1,2,8,3,4]),([2,3,4,5,6])
print(np.max(x,axis=0))
print(np.min(x,axis=0))
print(np.argmax(x,axis=0))
print(np.cumsum(x,axis=0))