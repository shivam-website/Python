a= int(input("Enter 1st number:"))
b= int(input("Enter 2nd number:"))
if(b==0):
    raise ZeroDivisionError("Cannot divide by zero")
else:
    print(f"The division of a/b is{a/b}")