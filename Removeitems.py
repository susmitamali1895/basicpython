thistuple = ("apple", "banana", "kiwi")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)