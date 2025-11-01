
age = int(input("Enter your age :"))
if(age%2==0):
    print("age is even")
if (age>=18):
    print("you are eligible for voting.")
elif(age%2==1):
    print("age is odd")
else:
    print("you are not eligible for voting.")

print("End of program")