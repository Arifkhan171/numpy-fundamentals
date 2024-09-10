import numpy as np
x=np.array([1,2,3,5,6])
x2=np.where(x==2) #where function tells the  index in the array
print(x2)

x=np.array([1,2,3,5,6])
x2=np.searchsorted(x,4) #tell you right index to put item
print(x2)

x=np.array([1,2,3,5,6])
np.random.shuffle(x)  # suffle the integers
print(x)