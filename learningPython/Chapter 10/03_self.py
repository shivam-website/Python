class Employe:
    language = "Python"#This is a class attribute
    salary = 100000

    def printdetails(self):#WE have to use self in every function inside class.
        print(f"The language is {self.language} and salary is {self.salary}.")

    @staticmethod
    def greet():
        print("Good Morning")
shivam = Employe()
shivam.language = "C++"#his is an instance attribute,this takes prefrecnce over class attribute
shivam.printdetails()
shivam.greet()
#Employe.printdetails(shivam)