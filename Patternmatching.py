# Pattern matching
# similar to switch case in other language 
#simple match case 
day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("wednesday")
    case _:
        print("Invalid day")


# menu - driven program
choice = 2
match choice:
    case 1:
        print("Add Item")
    case 2:
        print("Delete Item")
    case 3:
        print("Update Item")
    case _:
        print("Invalid choice")

# pattern matching with conditions
num = 10
match num:
    case x if x > 10:
        print("Positive")
    case x if x < 0:
        print("Negative")
    case _:
        print("Zero")