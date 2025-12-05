class GradeSystem:
    def __init__(self):
        self.transcript = []


    def assign_grade(self, student, course, score):
        record = {
            "student_id": student.student_id,
            "course": course,
            "score": score
        }
        self.transcript.append(record)
        print(f"Have entered: {score} for '{course.course_name}' of {student.name}")


    def calculate_gpa(self, student):
        total_points = 0
        total_credits = 0

        student_records = [rec for rec in self.transcript if rec["student_id"] == student.student_id]

        if not student_records:
            print(f"Student {student.name} have no scores")
            return 0.0

        print(f"\nDetailed Transcipt for {student.name}")
        for rec in student_records:
            course = rec["course"]
            score = rec["score"]
            print(f"{course.course_name}: {score}")

            total_points += score * course.credits
            total_credits += course.credits

        if total_credits == 0:
            return 0.0

        gpa = total_points / total_credits
        return round(gpa, 2)

