import re #regular expression
#check if the string starts wih "The" and ends with " Spain"

txt =  "The rain in Spain"
x= re.search("^The.*Spain$", txt)

if x:
    print("Yes! we have a match!")

else:
    print("No match")
    