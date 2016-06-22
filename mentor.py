from person import Person
import csv


class Mentor(Person):
    def __init__(self, first_name, last_name, year_of_birth, gender, knowledge_level, energy_level,
                 nickname=None, charisma=None):
        super().__init__(first_name, last_name, year_of_birth, gender, knowledge_level, energy_level)
        self.nickname = nickname
        self.charisma = charisma

    def create_by_csv(path):
        with open(path, newline="") as csvfile:
            mentorreader = csv.reader(csvfile, delimiter=",")
            rows = list(mentorreader)
            mentor_objects = [Mentor(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]) for row in rows]
            return mentor_objects
