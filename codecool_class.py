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
        mentors = Mentor.create_by_csv("data/mentors.csv")
        students = Student.create_by_csv("data/students.csv")
        print("\nSchool at {} in {} has been created, with {} mentors and {} students.".format(location,
                                                                                               year,
                                                                                               len(mentors),
                                                                                               len(students)))
        return CodecoolClass(location, year, mentors, students)

    def find_student_by_full_name(self, name):
        name = name.split(" ")
        try:
            x = [i for i in self.students if name[0] == i.first_name and name[1] == i.last_name][0]
            print('''
{0} {1} was found in the list of the students. He already had his coffee so he is ready to work.
'''.format(name[0], name[1]))
            return x
        except:
            print('''
{} {} is not in the student list. See you in our next course, {}!'''.format(name[0], name[1], name[0]))

    def find_mentor_by_full_name(self, name):
        name = name.split()
        try:
            x = [i for i in self.mentors if name[0] == i.first_name and name[1] == i.last_name][0]
            print("\n{0} {1} has been found amongst the mentors.".format(name[0], name[1]))
            return x
        except:
            print("No such name!")

    def overall_energy(self):
        mentors_energy = sum([i.energy_level for i in self.mentors])
        students_energy = sum([i.energy_level for i in self.students])
        return (mentors_energy + students_energy)

    def overall_knowledge(self):
        mentors_knowledge = sum([i.knowledge_level for i in self.mentors])
        students_knowledge = sum([i.knowledge_level for i in self.students])
        return (mentors_knowledge + students_knowledge)
