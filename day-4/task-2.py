class Person:
    def __init__(self, name):
        self.name = name

    def display_person(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, student_id):
        Person.__init__(self, name)
        self.student_id = student_id

    def display_student(self):
        self.display_person()
        print("Student ID:", self.student_id)


class SportsPlayer(Person):
    def __init__(self, name, sport_name):
        Person.__init__(self, name)
        self.sport_name = sport_name

    def display_sports_player(self):
        self.display_person()
        print("Sport Name:", self.sport_name)


class CollegeStudent(Student, SportsPlayer):
    def __init__(self, name, student_id, sport_name, college_name):
        Student.__init__(self, name, student_id)
        SportsPlayer.__init__(self, name, sport_name)
        self.college_name = college_name

    def display_college_student(self):
        self.display_person()
        print("Student ID:", self.student_id)
        print("Sport Name:", self.sport_name)
        print("College Name:", self.college_name)


cs = CollegeStudent(
    name="Lavanya",
    student_id=101,
    sport_name="Badminton",
    college_name="ABC Engineering College"
)

cs.display_college_student()
