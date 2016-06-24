from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from project import Project
from event import Event
from fun import Fun


def pause():
    input("")


print("""
*** Let\'s create our first Codecool Class! Are you ready? ***
       (Press 'Enter's and ascending numbers from '1'!)
""")
pause()

a = input(">>> codecool_bp = CodecoolClass.generate_local(): ")
if a == "1":
    pass
else:
    codecool_bp = CodecoolClass.generate_local()

pause()
b = input(">>> codecool_bp.find_student_by_full_name(self, 'Elon Musk'): ")
if b == "2":
    pass
else:
    codecool_bp.find_student_by_full_name('Elon Musk')

pause()
c = input(">>> codecool_bp.find_student_by_full_name(self, 'András Hinkel'): ")
if c == "3":
    pass
else:
    codecool_bp.find_student_by_full_name('András Hinkel')

pause()
d = input(">>> codecool_bp.find_mentor_by_full_name(self, 'Brian Python'): ")
if d == "4":
    pass
else:
    codecool_bp.find_mentor_by_full_name('Brian Python')

pause()
e = input("""It's 9 in the morning. The overall energy level is {}.
The day starts with a coding dojo.

>>> coding_dojo = Project("Miki", codecool_bp.students, 0, 100): """.format(codecool_bp.overall_energy()))
if e == "5":
    pass
else:
    coding_dojo = Project("Miki", codecool_bp.students, 0, 100)
# print("Overall energy level decreased with {} points.".format())

pause()
print("OK, it was tiring, let's have a coffee!")
f = input("\n>>> coffee_break = Break(): ")
if f == "6":
    pass
else:
    student_energy = [student.change_levels("energy_level", 2) for student in codecool_bp.students]
    print('''
Having a coffee increases the energy level of students!
New energy levels:
''')
    for student in student_energy:
        print(student.first_name, student.energy_level)


pause()
print("It's time to start the weekly project.")
g = input("\n>>> weekly_project = Project('Ruby', codecool_bp.students, 0, 9): ")
if g == "7":
    pass
else:
    weekly_project = Project("Ruby", codecool_bp.students, 0, 9)
# print("Overall knowledge level decreased with {} points.".format())

pause()
print("Such a long day! What's the time?")
h = input("\n>>> Event.time: ")
if h == "8":
    pass
else:
    print("\nThe time is around {} o'clock.".format(12))

pause()
print("LUNCHTIME!!!")
i = input("\n>>> lunch_time = Break(): ")
if i == "9":
    pass
else:
    print("\nThe lunchbreak is over. It's {} o'clock.".format(13))
# print("Overall energy level decreased with {} points.".format())

pause()
print("OK, keep goin', guys! Back to business!")
j = input("\n>>> under_performer = weekly_project.find_last_one(): ")
if j == "10":
    pass
else:
    under_performer = weekly_project.find_last_one()

pause()
k = input("\n>>> bestperformer = weekly_project.find_most_clever(): ")
if k == "11":
    pass
else:
    best_performer = weekly_project.find_most_clever()

pause()
l = input("\n>>> foosball_tournament = Fun(codecool_bp.students): ")
print("\n")
if l == "12":
    pass
else:
    foosball_tournament = Fun(codecool_bp.students)
    team = foosball_tournament.select_teams()
    foosball_tournament.game(team)

pause()
m = input("And this is the end of the story...To be continued: ")
pause()
exit()
