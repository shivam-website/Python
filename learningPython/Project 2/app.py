import random as r
count = 1
n = int(input("Enter the guessed num: "))
i = r.randint(1,100)
while (n!=i):
    if(n>i):
        print("Lower number please")
       
    elif(n<i):
        print("Higher number please")
    n = int(input("Enter the guessed num: "))
    count+=1        
else:
    print(f"{count} guesses taken to guess the number.")
    