class Person:
    GENDER = ['male', 'female', 'notsure']

    def __init__(self, first_name, last_name, year_of_birth, gender, knowledge_level, energy_level):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth

        if gender not in self.GENDER:
            print('Not a valid gender.')
            raise ValueError
        else:
            self.gender = gender

        self.year_of_birth = year_of_birth
        self.knowledge_level = knowledge_level
        self.energy_level = energy_level
