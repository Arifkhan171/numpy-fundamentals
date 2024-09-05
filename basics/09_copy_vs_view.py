import numpy as np
x=np.array([1,2,3,4,5])
print(x)
x2=np.copy(x)
print(x2) # copy function copy the code without any changes

print("")
w=np.array([1,2,3,4,5])
print(w)
w2=np.view(x) # view function copy the code with the changes in the  original function
print(w2)