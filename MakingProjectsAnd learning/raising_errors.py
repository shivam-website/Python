# try:
#     age = int(input("Enter your age:"))
#     if(age<0):
#         raise ValueError("Age cannot be negative!")
#     print(age)

# except ValueError as e:
#      print(e)
    
try:
    name = input("Enter your name: ")

    if any(char.isdigit() for char in name):
        raise ValueError("Enter your name only (no numbers allowed)")

    print("Your name is:", name)

except ValueError as e:
    print(e)
