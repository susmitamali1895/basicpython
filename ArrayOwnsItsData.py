#Print the value of the base attribute to check if an array owns its data or not
import numpy as np
arr = np.array([1,2,3,4,5])
x= arr.copy()
y = arr.view()
print(x.base)
print(y.base)
