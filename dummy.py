from event import Event


class Dummy(Event):
    '''testing things'''

    def __init__(self, ize, a_parameter):
        self.a_parameter = a_parameter
        super().time_manage(ize)
