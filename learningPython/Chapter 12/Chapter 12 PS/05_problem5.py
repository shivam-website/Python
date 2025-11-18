n = int(input("Enter a num to get table of it:"))
table = [n*i for i in range(1,11)]
print(table)
with open("Tables.txt","a")as f:
    f.write(str(table))