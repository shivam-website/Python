class Employee:
    company ="ITC"
    def show(self):
        print(f"The name is {self.name} and salary is {self.salary}")

class Programmer:
    company ="ITC Infotech"
    def show(self):
        print(f"The name is {self.name} and salary is {self.salary}")

    def showLanguage(self):
        print(f"The language is {self.language}")

a = Employee()
b = Programmer()
print(a.company)
print(b.company)