class Event:
    '''This class will be an abstract class.'''
    time = 0

    @classmethod
    def time_manage(cls, time):
        cls.time += time
