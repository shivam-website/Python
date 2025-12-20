#Using Walrus Operator
# if (n:= len([1,2,3,4,5]))>3:
#     print(f"List is too long, {n}")

# if(age:= int(input("Enter your age:")))>18:
#     print("Vaild")
# else:
#     print("Not vaild.")

if (age:= int(input("Enter your age:"))>18):
    print("Vaild")
else:
    print("Not vaild")