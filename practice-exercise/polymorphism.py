# Demonstrate your understanding of:
# class, inheritance and polymorhism

# create a class and objects
class Students:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student_information(self):
        return f"Student name is: {self.name} and is {self.age} years old"

# Create objects
student1 = Students("Uche", 32)
student2 = Students("Louisa", 28)
student3 = Students("Chika", 34)

# Call the method anf print the values
print(student1.student_information())
print(student2.student_information())
print(student3.student_information())

# Initialize student department class
class Student_dept(Students):

    def __init__(self, science, art, commercial):
        self.science = science
        self.art = art
        self.commercial = commercial
    
    def graduants_list(self):
        return f"{self.name } is a {self.age} year old girl. She is an {self.art} student.\
        She did consider being a {self.science} and {self.commercial} student but it didn't quite feel right"
    
dept_science = Student_dept("physics", 5)
dept_art = Student_dept("literature", 4)
dept_commercial = Student_dept("accounting", 10)

print(dept_science.graduants_list())
print(dept_art.graduants_list())
print(dept_commercial.graduants_list())