#create a filter array that will return only values higher than 42
import numpy as np
arr = np.array([41,42,43,44])
filter_arr = arr>42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
