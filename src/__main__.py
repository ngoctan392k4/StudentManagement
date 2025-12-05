from src.ClassModule.classInfo import ClassInfo
from src.StudentModule.student import Student
from src.CourseModule.course import Course
from src.GradeModule.grade import GradeSystem

if __name__ == "__main__":
    newClass1 = ClassInfo("IS CR 250 A", "TRƯƠNG VĂN TRƯƠNG")
    newCourse1 = Course("Foundation of computer system", 3, "LEC")

    newClass2 = ClassInfo("HIS 222", "TRUNG HIẾU")
    newCourse2 = Course("World History", 2, "LEC")

    newStudent = Student("SV001", "HNNT", "ADP", "CS")

    newStudent.join_class(newClass1)
    newStudent.join_class(newClass2)

    grade_sys = GradeSystem()

    grade_sys.assign_grade(newStudent, newCourse1, 8.0)
    grade_sys.assign_grade(newStudent, newCourse2, 7.0)

    gpa = grade_sys.calculate_gpa(newStudent)

    print(f"Grade Point Average: {gpa}")