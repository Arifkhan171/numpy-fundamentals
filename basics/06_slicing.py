#  slicing in numpy
import numpy as np
z=np.array([1,2,23,4,5,6,8,9])
print(z[1:5]) # print from index 1 to 5 all columns
print(z[0:5]) # print from index 0 to 5
print(z[:5]) # print from index 0 to 5
print(z[1:]) # print from index 1 to last
print(z[::]) # print from index 0 to last
print(z[1::2]) # print from index 1 to last with gap 2
print("")


z=np.array([[1,2,23,4],[5,6,8,9]])
print(z[1,:2]) # print from array index 1 ,from start element to to index 2 but index 2 not included