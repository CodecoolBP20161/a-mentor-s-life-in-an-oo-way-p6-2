from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from project import Project

def pause():
    input("")

a = input("\n>>> codecool_bp = CodecoolClass.generate_local(): ")
if a == "1":
    codecool_bp = CodecoolClass.generate_local()

pause()
b = input("\n\n>>> codecool_bp.find_student_by_full_name(self, 'Elon Musk'): ")
if b == "2":
    codecool_bp.find_student_by_full_name('Elon Musk')

pause()
c = input("\n\n>>> codecool_bp.find_student_by_full_name(self, 'András Hinkel'): ")
if c == "3":
    codecool_bp.find_student_by_full_name('András Hinkel')

pause()
d = input("\n>>> codecool_bp.find_mentor_by_full_name(self, 'Brian Python'): ")
if d == "4":
    codecool_bp.find_mentor_by_full_name('Brian Python')

pause()
print("It's 9 in the morning. The overall energy level is {}. The day starts with a coding dojo.".format())
dojo = Project("Ruby", codecool_bp.students, 0)
print("Overall energy level decreased to: {}".format())


pause()
# Dojo decreases the energy level of the class so the mentor calls a coffee break
# Coffee break increases the energy_level, knowledge_level is not changing
# Assignment: checking knowledge_level and the difficulty: if someone doesn't pass: private mentoring
# Energy level is low: foosball tournament
