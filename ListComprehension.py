#without list comprehension
#fruits= ["apple", "banana", "cherry", "kiwi", "mango"]
#newlist = []

#for x in fruits:
    #if "a" in x:
       #newlist.append(x)
#print(newlist)

#with list comprehension

fruits= ["apple", "banana", "cherry", "kiwi", "mango"]
newlist =[x for x in fruits if "a" in x ]
print(newlist)