#Dictionary having key and value pair
dict= {
    "name": "bob",
    "age" : 30

}
# we cant direct remove or add a value from a dictionary
# if you want to remove or add any value then you have to remove he perticular key value pair
# for add also we need to add key value pair

# for add in dictionary
dict = {
    "name": "Jack",
    "age" : 32
}
dict.update({"country":"India"})
print(dict)

# for remove any value from dictionary
dict  ={
    "name": "Jack",
    "age" : 32
}
dict.pop("age")
print(dict)
