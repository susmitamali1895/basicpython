# diff bet list & tuple give ex
List = ["Alice", "banana", 1, 2] #List []bracket, contains any datatype, 
#you can easily add or remove from list
# you 
List.remove(2)
print(List)


tuple1 = ("Alice", "Banana", True, 1, 2, 3) # tuple () bracket
# it also supports all datat types
# but in tuple we cant directly remove or add items , we need to convert this tuple to list
x = list(tuple1)
x.remove("Banana")
tuple1= tuple(x)
print(tuple1)