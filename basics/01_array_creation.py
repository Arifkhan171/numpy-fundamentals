# # numpy array creation with fixed size \all funcrion are ones, zeros,empty, eye,linespace,range
import numpy as np

x=np.ones([3,4])
print(x) # creats matrix of ones of 3 rows and 4 columns

x=np.zeros([3,4])
print(x)   # creats matrix of zeros of 3 rows and 4 columns

x=np.empty([3,4])
print(x) # creats matrix of empty numbers but temporary copies previous memory data of 3 rows and 4 columns
#
x=np.eye(4)
print(x) # creats matrix of diagonal elements of 4 rows and 4 columns
#
x=np.linspace(0,20,5)
print(x)   # creats matrix of numbers with spacific steps


x=np.arange(5)
print(x)  # creats matrix of spacefic  elements of given range


                        # creation with random no
x=np.random.rand(5)# creats 5 numbers b/w 0/1
print(x)

x=np.random.randn(5)# creats   close to 0
print(x)

x=np.random.ranf(8)# creats close to 0 both +-
print(x)


x=np.random.randint(0,5,3) # creats b/w given range
print(x)

