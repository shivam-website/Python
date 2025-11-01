mark1 = int(input("Enter mark of subject 1 :"))
mark2 = int(input("Enter mark of subject 2 :"))
mark3 = int(input("Enter mark of subject 3 :"))

total_percentage = (100*(mark1 + mark2 + mark3))/300
print("Total percentage is ",total_percentage)
if(total_percentage>=40 and mark1>=33 and mark2>=33 and mark3>=33):
    print("Pass")
else:
    print("Fail")