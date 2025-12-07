l = [5,3,10,2,4,543,435,7680]
def div(n):
    if(n%5==0):
        return True
    return False
divisible = filter(div,l)
print(list(divisible))