#split the 2D array into three 2D arrays
import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,1,12],[13,14,15],[16,17,18]])
newarr= np.array_split(arr,3)
print(newarr)
