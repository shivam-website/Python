class Employe:
    language = "Python"#This is a class attribute
    salary = 100000

    def __init__(self,name,salary,language):#called as dunder method and it is called automatically
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def printdetails(self):#WE have to use self in every function inside class.
        print(f"The language is {self.language} and salary is {self.salary}.")

    @staticmethod
    def greet():
        print("Good Morning")
shivam = Employe("Shivam",110000,"Javascript")
# shivam.language = "C++"#his is an instance attribute,this takes prefrecnce over class attribute
shivam.printdetails()
#Employe.printdetails(shivam)
shivam.greet()
