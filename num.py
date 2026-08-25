import numpy as np
a=np.array([1,2,3,4])
print(a)
print(a.ndim)
print(sum(a))
print(max(a))
print(min(a))
for i in a:
    print(i)
a2=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a2)
print(a2.ndim)
for i in a2:
    for j in i:
        print(j)
print(sum(a2))
a3=sum(a2)
print(sum(a3))
for i in a2:
    for j in i:
        if j%2==0:
            print(j)