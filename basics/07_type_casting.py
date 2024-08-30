# type casting in numpy
import numpy as np
x=np.array([1,2,3,4],dtype=float)
print(x,x.dtype)

x=np.array([1,2,3,4])
x2=np.float32(x)
print(x2,x2.dtype)

x=np.array([1,2,3,4])
x2=x.astype(float)
print(x2,x2.dtype)