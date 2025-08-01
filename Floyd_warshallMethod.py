# Find the shortest path between all pairs of elements 
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix
arr = np.array([
    [0,1,2],
    [1,0,0],
    [2,0,0]
])
newarr = csr_matrix(arr)
print(floyd_warshall(newarr, return_predecessors = True))
