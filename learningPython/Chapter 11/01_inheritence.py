class Employee:
    company ="ITC"
    name = "Shivam"
    salary = "Rs 1122"
    def show(self):
        print(f"The name is {self.name} and salary is {self.salary}")

class Programmer(Employee):
    company ="ITC Infotech"
    def show(self):
        print(f"The name is {self.name} and salary is {self.salary}")

    def showLanguage(self):
        print(f"The language is {self.language}")

a = Employee()
b = Programmer()
b.show()
print(a.company)
print(b.company)