from person import Person
import csv


class Mentor(Person):
    def __init__(self, nickname, charisma, *args):
        super().__init__(*args)
        self.nickname = nickname
        self.charisma = charisma

    @classmethod
    def create_by_csv(cls, path):
        with open(path, newline="") as csvfile:
            mentorreader = csv.reader(csvfile, delimiter=",")
            rows = list(mentorreader)
            mentor_objects = [Mentor(row[6], row[7], row[0], row[1], row[2], row[3], row[4], row[5]) for row in rows]
<<<<<<< HEAD
            print("\nMentors have been initialized from CSV. Here they are:\n")

            for row in rows:
                print("{} {}".format(row[0], row[1]))

=======
>>>>>>> d9f2223afef93bea92c8ddf27f18496f850233b7
            return mentor_objects
