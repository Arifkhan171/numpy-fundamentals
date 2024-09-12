# matrix operations
import numpy as np
x=np.matrix([1,2,3,4])
x1=np.matrix([[2]])
print(x1.dot(x))   # multiple matrix 1 and 2

x=np.matrix([1,2,3,4])
x1=np.matrix([3,4,5,6])
x3=np.transpose(x1) # transpose means change columns to rows and viseversa
print(x3)
print(x.dot(x3))


x=np.matrix([1,2,3,4])
print(np.transpose(x))

