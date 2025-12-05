class Course:
    def __init__(self, course_name, credits, course_type):
        self.course_name = course_name
        self.credits = credits
        self.course_type = course_type

    def show_course(self):
        print(f"Course: {self.course_name} ({self.credits} credits) - Type: {self.course_type}")