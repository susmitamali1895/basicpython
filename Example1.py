class person:
    def __init__(self,fname,lname):
        self.firstname = fname 
        self.lastname = lname 
    def printname(self):
        print(self.firstname,self.lastname)

x = person("john", "Doe")
x.printname()

#Use the person class to create an object and the execute the printname method
