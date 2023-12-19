class Node:

    def __init__(self, name: float = 0.0, type: int = 0, value: int = 0, fanouts: dict = {}, faulty: bool = False, fault: int = 0):
        '''
            type:
                0: input
                1: output
        '''
        self.name = name
        self.type = type
        self.value = value
        self.fanouts = fanouts
        self.faulty = faulty
        self.fault = None

    def set_value(self, value):
        self.value = value
        if (len(self.fanouts)):
            for fanout in self.fanouts:
                self.fanouts[fanout].value = self.value
        return self.value