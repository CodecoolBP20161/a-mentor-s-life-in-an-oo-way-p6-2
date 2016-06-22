from mentor import Mentor
from student import Student
from datetime import date


class CodecoolClass:

    def __init__(self, location, year, mentors=[], students=[]):
        self.location = location
        self.year = year
        self.mentors = mentors
        self.students = students

    @staticmethod
    def generate_local():
        year = date.today().year
        location = "Budapest"
        mentors = []
        students = Student.create_by_csv("data/students.csv")
        return CodecoolClass(location, year, mentors, students)

    def find_student_by_full_name(self, name):
        name = name.split(" ")
        try:
            x = [i for i in self.students if name[0] == i.first_name and name[1] == i.last_name][0]
            print("{0} {1} {2}".format(name[0], name[1], "was found in students list"))
            return x
        except:
            print("No such name!")

    def find_mentor_by_full_name(self, name):
        name = name.split()
        try:
            x = [i for i in self.mentors if name[0] == i.first_name and name[1] == i.last_name][0]
            print("{0} {1} {2}".format(name[0], name[1], "was found in mentors list"))
            return x
        except:
            print("No such name!")
