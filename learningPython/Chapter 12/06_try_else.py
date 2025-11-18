try:
    a = int(input("Enter a num:"))
    print(a)

except Exception as e:
    print(e)

else:
    print("Try block finally worked.")#Only run when try is sucessful