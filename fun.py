from mentor import Mentor
from student import Student
from codecool_class import *
from datetime import date
import random


class Fun:

    def __init__(self, participants):
        self.participants = participants

    def select_teams(self):
        # reads the students csv and selects teams of 2. Teams are only accepted if it is in the sol list
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
        print("\n")
        return s

    def decide(self, team1, team2, xsco, ysco):
        # decides between two teams and returns them with the score
        while xsco < 6 and ysco < 6:
            x = int(team1[0].energy_level + team1[1].energy_level)*random.randint(3, 20)/10
            y = int(team2[0].energy_level + team2[1].energy_level)*random.randint(3, 20)/10
            if x >= y:
                xsco += 1
            else:
                ysco += 1

        # check score
        if xsco >= ysco:
            return (team1, xsco, ysco)
        else:
            return (team2, xsco, ysco)

    def game(self, team):
        # the main method of the fun class
        self.winner = []
        self.score = []

        while team:

            sample = random.sample(team, 2)
            team.remove(sample[0])
            team.remove(sample[1])
            winner_student = self.decide(sample[0], sample[1], 0, 0)[0]
            x = self.decide(sample[0], sample[1], 0, 0)[1:]
            self.score.append(x)
            self.winner.append(winner_student)

        if len(self.winner) == 4:
            # prints Quarterfinals
            x = [i[0].first_name for i in self.winner]
            y = [i[1].first_name for i in self.winner]
            c = [i for i in self.score]

            for i, j, k in zip(x, y, c):
                print(i + " and " + j + " won the Quarterfinals!(" + str(k[0]) + "-" + str(k[1]) + ")")
            print("\n")

        elif len(self.winner) == 2:
            # prints Semifinals
            q = [i[0].first_name for i in self.winner]
            w = [i[1].first_name for i in self.winner]
            zs = [i for i in self.score]

            for i, j, k in zip(q, w, zs):
                print(i + " and " + j + " won the Semifinals!(" + str(k[0]) + "-" + str(k[1]) + ")")
            print("\n")

        if len(self.winner) == 1:
            # prints the winner of the game and increases the corresponding energy levels
            a = self.score[0]

            print(self.winner[0][0].first_name + " and " + self.winner[0][1].first_name + " won the tournament!(" +
                  str(a[0]) + "-" + str(a[1]) + ")")
            epicwin = self.winner[0]
            print("\n")
            print(epicwin[0].first_name + "'s energy level increased by 2")
            print(epicwin[1].first_name + "'s energy level increased by 2")
            epicwin[0].change_levels("energy_level", 2)
            epicwin[1].change_levels("energy_level", 2)
            return self.winner

        else:
            self.game(self.winner)
