class ClassInfo:
    def __init__(self, class_name, instructor):
        self.class_name = class_name
        self.instructor = instructor

    def show_info(self):
        return f"Class: {self.class_name} with Instructor: {self.instructor}!"