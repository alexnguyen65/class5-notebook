import numpy as np

myarray = np.array([1,22.4,5,35,4,6.7,3,8,40])
print(myarray)
print(myarray.ndim)
print(myarray.shape)
print(myarray.size)
print(myarray.dtype)

myarray = np.array([['a', 'b'],['c', 'd'],[3, 3]])
print(myarray)
print(myarray.ndim)
print(myarray.shape)
print(myarray.size)
print(myarray.dtype)

myarray = np.array([['a', 'b'],['c', 'd'],[3, 3]])
print(myarray)
print(myarray.ndim)
print(myarray.shape)
print(myarray.size)
print(myarray.dtype)

print(np.arange(15,30))
print(np.linspace(0,10,20))
print(np.random.rand(10))

print(np.zeros(shape = (2,3), dtype=int))
print(np.ones(shape = (2,3), dtype = int))
print(np.eye(2,3,dtype=int))
print(np.random.rand(2,3))

array_of_sevens = np.ones(20)*7
reshape_array = array_of_sevens.reshape(4,5)
print(reshape_array[0])

