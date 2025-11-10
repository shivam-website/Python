class Number():
    def __init__(self,num):
        self.num = num

    def __add__(self,num2):
        return self.num + num2.num


    
n = Number(10)
m = Number(20)
print(n+m)