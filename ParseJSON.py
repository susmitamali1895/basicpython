import json 
# some json
x = '{"name":"JOHN", "age":36, "city":"New York"}'

#parse x
y = json.loads(x)

#the result is a python dictionary
print(y["age"])