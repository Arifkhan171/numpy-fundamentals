# insert and delet functions
import numpy as np
x=np.array([1,2,3,5,6])
x2=np.insert(x,3,44) # insert the 44 at index 3 without losing any int
print(x2)

x=np.array([[1,2,3,5,6]])
x2=np.insert(x,3,44,axis=1)# insert the 44 at index 3 without losing any int
print(x2)

x=np.array([[1,2,3],[4,5,6]])
x2=np.insert(x,3,44,axis=1)
print(x2)



x=np.array([[1,2,3,5,6]])
x2=np.delete(x,3)
print(x2) # delet the number from index 3