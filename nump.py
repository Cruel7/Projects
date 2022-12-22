import numpy as np

a=np.array([1,2,3,4,32],dtype="int16")
b=np.array([6,7,8,9,1])
c=np.matmul(a,b)
print(c)

xdd=np.array([1,23,4,5,6],dtype="int16")
print(xdd.dtype)
print(a.dtype, "+", b.dtype)
print(a.size, b.size)
print(a.nbytes)

print(np.random.randint(7,size=(3,3),dtype="int32"))

output=np.ones((5,5))
print(output)
z=np.zeros((3,3))
z[1,1]=9
print(z)
output[1:4,1:4]=z
print(output)