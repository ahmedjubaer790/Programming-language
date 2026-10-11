import numpy as np 
array=np.array([1,2,3,4,5])
x=array.copy()
y=array.view()

print(x.base)
print(y.base)