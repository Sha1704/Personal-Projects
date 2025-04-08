class Person:
    
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def print_directory(self):
        print(self.name)
        print(self.email)

class Student(Person):

    def __init__(self, name, email, major, class_level):
        Person.__init__(self, name, email)
        self.major = major
        self.class_level = class_level

    def print_directory(self):
        Person.print_directory(self)
        print(self.major)
        print(self.class_level)
    

class Employee(Person):

    def __init__(self, name, email, department, office):
        Person.__init__(self, name, email)
        self.department = department
        self.office = office

    def print_directory(self):
        Person.print_directory(self)
        print(self.department)
        print(self.office)

class Faculty(Employee):

    def __init__(self, name, email, department, office,  research_area):
        Employee.__init__(self, name, email, department, office)
        self.research_area = research_area

    def print_directory(self):
        Employee.print_directory(self)
        print(self.research_area)

def main():
    
    p1 = Person('John Doe', 'jdoe@ilstu.edu')
    p2 = Person('Joseph Smith', 'joeSmith@ilstu.edu')

    s1 = Student ('John Doe', 'jdoe@ilstu.edu', 'Political Science', 'Junior')
    s2 = Student ('Joseph Smith', 'joeSmith@ilstu.edu', 'Computer Science', 'Senior')

    e1 = Employee ('John Doe', 'jdoe@ilstu.edu', 'English', 'STV 404B')
    e2 = Employee ('Joseph Smith ', 'joeSmith@ilstu.edu', 'Information Technology', 'OU 137')

    f1 = Faculty('Mary Elaine Califf', 'mecalif@ilstu.edu', 'Information Technology', 'WIH 17A', 'Machine Learning, Natural Language Processing, CS Education')
    f2 = Faculty('Carl Johnson', 'cj1892@ilstu.edu', 'African American Studies', 'STV 101', 'African american culture')

    object_list = []
    object_list.append(p1)
    object_list.append(p2)
    object_list.append(s1)
    object_list.append(s2)
    object_list.append(e1)
    object_list.append(e2)
    object_list.append(f1)
    object_list.append(f2)

    for obj in object_list:
        obj.print_directory()
        print()

if __name__ == '__main__':
    main()