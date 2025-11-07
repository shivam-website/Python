class Employe:
    language = "Python"#This is a class attribute
    salary = 100000

shivam = Employe()
shivam.name = "Shivam"
shivam.language = "C++"#his is an instance attribute,this takes prefrecnce over class attribute
print(shivam.name)
print(shivam.language)
print(shivam.salary)
 