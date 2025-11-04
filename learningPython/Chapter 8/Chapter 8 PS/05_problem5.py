def traingle(n):
    if(n==0):
        return
    print("*"*n)
    traingle(n-1)

traingle(5)
