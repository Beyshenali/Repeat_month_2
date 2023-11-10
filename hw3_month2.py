class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def login(self):
        print(f"{self.name} вошел в систему.")


class Student(User):
    def __init__(self, name, email, password, student_id):
        User.__init__(self, name, email, password)
        self.student_id = student_id
        self.courses_enrolled = []

    def enroll_in_course(self, course):
        self.courses_enrolled.append(course)
        print(f"{self.name} поступил в {course}.")


class Teacher(User):
    def __init__(self, name, email, password, teacher_id):
        User.__init__(self, name, email, password)
        self.teacher_id = teacher_id
        self.courses_teaching = []

    def assign_grade(self, student, course, grade):
        print(f"Учитель {self.name} поставил оценку {grade}  {student} у для {course}.")


class Admin(User):
    def __init__(self, name, email, password, admin_id):
        User.__init__(self, name, email, password)
        self.admin_id = admin_id

    def create_course(self, course_name):
        print(f"Admin {self.name} создал новый курс: {course_name}.")


class TeachingAssistant(Student, Teacher):
    def __init__(self, name, email, password, student_id, teacher_id):
        Student.__init__(self, name, email, password, student_id)
        Teacher.__init__(self, name, email, password, teacher_id)

student = Student("Semetei Manasov", "semetei@gmail.com", "tiybe", "001")
teacher = Teacher("Dr. Bakai", "bakai@gmail.com", "mugalim", "002")
admin = Admin("Admin Kursan", "kursan@gmail.com", "adminkursan", "003")
asistant = TeachingAssistant("asistant Kerim", "kerim@gmail.com", "achpa", "004", "005")

student.login()
student.enroll_in_course("Matematika 100")

teacher.login()
teacher.assign_grade("Semetei Manasov", "Matematika 100", "A")

admin.login()
admin.create_course("Physics 99")

asistant.login()
asistant.enroll_in_course("Physics 99")
asistant.assign_grade("Semetei Manasov", "Physics 101", "B")
