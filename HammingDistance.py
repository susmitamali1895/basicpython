from scipy.spatial.distance import hamming
p1 = (True, False, True)
p2 = (False, True, False)
res = hamming(p1,p2)
print(res)