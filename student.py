from person import Person
import csv


class Student(Person):

    def __init__(self, *args):
        super().__init__(*args)

    @classmethod
    def create_by_csv(cls, file_name):
        with open(file_name) as csvfile:
            studentsreader = csv.reader(csvfile, delimiter=",")
            rows = list(studentsreader)
            x = [Student(i[0], i[1], i[2], i[3], i[4], i[5]) for i in rows]
            return x
