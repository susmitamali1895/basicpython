#change datatype float to integer by using 'i' as parameter value
import numpy as np
arr= np.array([1.1,2.1,3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)
