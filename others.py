from event import Event


class Others(Event):
    '''This class is for time sensitive things.'''

    def __init__(self, name, change_energy, change_knowledge):
        super().time_manage(time)
        self.name = name
        self.change_energy = change_energy
        self.change_knowledge = change_knowledge

a = Others(1, 0)

print(a.energy, a.knowledge)

a.change_levels()

print(a.energy, a.knowledge)
