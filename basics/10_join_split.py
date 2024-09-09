# concatenate thr arrays
import numpy as np
x=np.array([1,2,3,4,5])
x2=np.array([1,2,3,7,8])
x3=np.concatenate([x,x2])# make  one array
print(x3)


x=np.array([[1,2,3,4,5]])
x2=np.array([[1,2,3,7,8]])
x3=np.concatenate([x,x2],axis=0)
print(x3)
x3=np.dstack([x,x2]) #concate and make two columns
print(x3)
# #
x3=np.hstack([x,x2]) # conctenate in row wise
print(x3)
#
x3=np.vstack([x,x2]) # conctenate in columns wise
print(x3)
#
x3=np.stack([x,x2])
print(x3)

print("")
x=np.array([1,2,3,4,5,6])
x2=np.split(x,2)
print(x2)

print("")
x=np.array([[1,2,3],[4,5,6]])
x2=np.split(x,2,axis=0) # split the arrays in row wise
print(x2)
print('')
x=np.array([[1,2,3,4,5,6]])
x2=np.split(x,2,axis=1)
print(x2)  # split the arrays in columns wise
