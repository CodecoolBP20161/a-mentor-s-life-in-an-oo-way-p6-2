from mentor import Mentor
from student import Student
from datetime import date


class CodecoolClass:

    def __init__(self, location, year, mentors=[], students=[]):
        self.location = location
        self.year = year
        self.mentors = mentors
        self.students = students

    def generate_local():
        year = date.today().year
        location = "Budapest"
        return CodecoolClass(location,year)

# cs = CodecoolClass.generate_local()
# print(cs)

    def find_student_by_full_name(self,name,students):
        name = name.split(" ")
        try:
            return [i for i in self.students if name[0] == i.firstname and name[1] == i.lastname][0]
        except:
            print("No such name!")
