class Employee():
    salary = 100000
    incriment = 20
    @property
    def salaryAfterIncriment(self):
        self.salary =self.salary+ self.salary*(self.incriment/100)
        return self.salary

e = Employee()
print(e.salary)
print(e.salaryAfterIncriment)