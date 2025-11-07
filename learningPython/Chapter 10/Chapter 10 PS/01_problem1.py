class Programmer():
    company = "Microsoft"
    def __init__(self,name,salary,pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

p = Programmer("Shivam",100000,112233)
print(p.company)
print(p.name)
print(p.salary)
print(p.pincode)

r= Programmer("rohan",100000,1112233)
print(r.company)
print(r.name)
print(r.salary)
print(r.pincode)