from mentor import Mentor
from student import Student
from codecool_class import *
from datetime import date
import random

students = CodecoolClass.generate_local().students


class Fun(object):

    def __init__(self, participants, winner=None):

        self.participants = participants
        if winner is None:
            self.winner = []

    def select_teams(self):
        x = len(self.participants) % 2
        y = random.sample(self.participants, len(self.participants)-x)
        s = []
        sol = [2**i for i in range(1, 10)]
        while y:
            z = random.sample(y, 2)
            y.remove(z[0])
            y.remove(z[1])
            s.append(z)
        while len(s) not in sol:
            v = random.choice(s)
            not_interested = []
            not_interested.append(v)
            s.remove(v)
            for names in not_interested:
                print("%s was not interested in playing." % (names[0].first_name))
        return s

    @staticmethod
    def decide(team1, team2):
        x = int(team1[0].energy_level + team1[1].energy_level)*random.randint(7, 12)/10
        y = int(team2[0].energy_level + team2[1].energy_level)*random.randint(7, 12)/10
        if x >= y:
            return team1
        else:
            return team2

    def game(self, team):
        """  """
        self.winner = []

        while team:

            sample = random.sample(team, 2)
            team.remove(sample[0])
            team.remove(sample[1])
            winner_student = self.decide(sample[0], sample[1])
            self.winner.append(winner_student)

        if len(self.winner) == 4:

            x = [i[0].first_name for i in self.winner]
            y = [i[1].first_name for i in self.winner]

            for i, j in zip(x, y):
                print(i + " and " + j + " won the Quarterfinals!")

        elif len(self.winner) == 2:

            q = [i[0].first_name for i in self.winner]
            w = [i[1].first_name for i in self.winner]

            for i, j in zip(q, w):
                print(i + " and " + j + " won the Semifinals!")

        if len(self.winner) == 1:

            print(self.winner[0][0].first_name + " and " + self.winner[0][1].first_name + " won the tournament!")
            epicwin = self.winner[0]
            print(epicwin[0].first_name + "'s energy level increased by 2")
            print(epicwin[1].first_name + "'s energy level increased by 2")
            epicwin[0].change_levels("energy_level", 2)
            epicwin[1].change_levels("energy_level", 2)
            return self.winner

        else:
            self.game(self.winner)

mm = Fun(students)
asd = mm.select_teams()
mm.game(asd)
