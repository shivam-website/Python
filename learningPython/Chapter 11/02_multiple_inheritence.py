class Employee:
    company ="ITC"
    name = "DefaultName"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(self.language)

class Programmer(Employee,Coder):
    company ="ITC Infotech"

    def showLanguage(self):
        print(f"The language is {self.language}")

a = Employee()
b = Programmer()
b.show()
b.showLanguage()
b.printLanguage()
