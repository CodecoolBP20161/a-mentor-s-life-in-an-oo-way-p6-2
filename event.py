class Event:
    '''This class will be an abstract class.'''
    time = 0

    @classmethod
    def time_manage(cls, ize):
        cls.time += ize

    @classmethod
    def change_levels(cls,obj,attribute,delta):
        obj.attribute += delta
