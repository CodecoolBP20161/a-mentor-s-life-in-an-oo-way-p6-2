from mentor import Mentor
from student import Student
from codecool_class import *
from datetime import date
import random

o = CodecoolClass.generate_local().students


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
            s.remove(v)
            print("%s was not interested in playing." % (v[0].first_name))
            print("%s was not interested in playing." % (v[1].first_name))
        return s

    @staticmethod
    def decide(team1, team2):
        x = int(team1[0].energy_level + team1[1].energy_level)*random.randint(7, 12)/10
        y = int(team2[0].energy_level + team2[1].energy_level)*random.randint(7, 12)/10
        if x >= y:
            return team1
        else:
            return team2

    # @staticmethod
    def game(self, team):
        """  """
        # print(len(team))

        self.winner = []

        while team:

            sample = random.sample(team, 2)
            team.remove(sample[0])
            team.remove(sample[1])
            self.winner.append(self.decide(sample[0], sample[1]))

        if len(self.winner) == 1:

            print(self.winner[0][0].first_name + " and " + self.winner[0][1].first_name + " won the tournament!")
            return self.winner

        else:
            self.game(self.winner)

mm = Fun(o)
asd = mm.select_teams()
mm.game(asd)
