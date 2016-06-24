from event import Event
import csv

class Break(Event):
    '''This class is for breaks.'''

    def __init__(self, name, change_energy, change_knowledge, change_charisma, change_time):
        self.name = name
        self.change_energy = change_energy
        self.change_knowledge = change_knowledge
        self.change_charisma = change_charisma
        self.change_time = change_time

    @classmethod
    def create_by_csv(cls, path):
        with open(path, newline="") as csvfile:
            break_csv = csv.reader(csvfile, delimiter=",")
            rows = list(break_csv)
            break_objects = [Break(row[0], row[1], row[2], row[3], row[4]) for row in rows]
            return break_objects

    def use_event(self):
        self.super().time_manage(time)

a = Break.create_by_csv("data/break.csv")

print(a)
