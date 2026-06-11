
# iteration in numpy
import numpy as np
x=np.array([1,2,3,4,5])
for i in x:
    print(i)
print("")

x=np.array([[1,2,3,4,5],[6,7,8,9,0]])
for i in x:
    for k in i:
        print(k)
print("")

x=np.array([[1,2,3,4,5],[6,7,8,9,0]])
for i in np.nditer(x):
    print(i)
for i,d in np.ndenumerate(x):
    print(i,d)


x=np.array([[[1,2,3,4,5],[6,7,8,9,0]]])
for i in x:
    for k in i:
        for n in k:
            print(n)
print('')

x=np.array([[[1,2,3,4,5],[6,7,8,9,0]]])
for i in np.nditer(x):
    print(i)
for i,d in np.ndenumerate(x):
    print(i,d)