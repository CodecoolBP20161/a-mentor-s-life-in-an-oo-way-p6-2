from mentor import Mentor
from student import Student
from codecool_class import *
from datetime import date
import random

o = CodecoolClass.generate_local().students
print(o)


class Project:

    def __init__(self, mentor, students, difficulity):
        self.mentor = mentor
        self.students = [i for i in students if int(
            i.knowledge_level) >= difficulity]
        self.difficulity = difficulity
        print("A new Project has been started with %s participants." %
              (len(self.students)))

    def find_most_clever(self):
        x = sorted(self.students, key=lambda x: int(x.knowledge_level))
        print("""It turns out that the cleverest student in this project
is %s %s and will present on a meetup next month.""" % (x[-1].first_name, x[-1].last_name))

    def find_last_one(self):
        x = sorted(self.students, key=lambda x: int(x.knowledge_level))
        y = [i.knowledge_level for i in x]
        print(y)
        print("""%s %s was underperforming and mentor %s advises more
private mentoring in the future.""" % (x[0].first_name, x[0].last_name, self.mentor))

dojo = Project("Miki", o, 0)
dojo.find_most_clever()
dojo.find_last_one()
