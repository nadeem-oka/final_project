import uuid

class Student:
    def __init__(self, student_name, student_age, student_number, courses_list):
        self.student_id = str(uuid.uuid4())
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = courses_list

