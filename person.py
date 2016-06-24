class Person:
    ''' This class represents a group of people. '''

    # acceptable gender types
    GENDER = ['male', 'female', 'notsure']

    def __init__(self, first_name, last_name, year_of_birth, gender, knowledge_level, energy_level):

        try:
            for arg in [first_name, last_name, year_of_birth, gender, knowledge_level, energy_level]:
                if not arg:
                    raise TypeError

        except TypeError:
            print('Empty parameter is forbidden.')

        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = int(year_of_birth)

        try:
            if gender not in self.GENDER:
                raise ValueError

        except ValueError:
            print('Not a valid gender.')

        self.gender = gender
        self.knowledge_level = int(knowledge_level)
        self.energy_level = int(energy_level)

    def change_levels(self, attribute, delta):
        setattr(self, attribute, getattr(self, attribute)+delta)
        return self
