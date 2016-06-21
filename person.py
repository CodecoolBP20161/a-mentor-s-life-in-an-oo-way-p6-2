class Person:
    ''' This class represents a group of people. '''

    GENDER = ['male', 'female', 'notsure']

    def __init__(self, first_name, last_name, year_of_birth, gender, knowledge_level, energy_level):
        for arg in [first_name, last_name, year_of_birth, gender, knowledge_level, energy_level]:
            if not arg:
                raise ValueError('Empty parameter is forbidden.')
            else:
                self.first_name = first_name
                self.last_name = last_name
                self.year_of_birth = year_of_birth

                if gender not in self.GENDER:
                    raise ValueError('Not a valid gender.')
                else:
                    self.gender = gender

                self.knowledge_level = knowledge_level
                self.energy_level = energy_level
