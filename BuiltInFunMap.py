#map
#applies a unction to every item in an iterable
nums = [1,2,3,4]
squared =map(lambda x: x**2, nums)
print(list(squared))