class Student:
    def __init__(self, student_id, name, department, major):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.major = major
        self.my_class = []

    def join_class(self, class_info):
        self.my_class = class_info

    def show_profile(self):
        class_str = self.my_class.class_name if self.my_class else "No Classes"
        print(f"STUDENT INFORMATION")
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Major: {self.major}")
        print(f"Class: {class_str}")
