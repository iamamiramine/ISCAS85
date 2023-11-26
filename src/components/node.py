class Node:

    def __init__(self, name: int = 0, type: int = 0, value: int = 0, fanouts: dict = {}):
        '''
            type:
                0: input
                1: output
        '''
        self.name = name
        self.type = type
        self.value = value
        self.fanouts = fanouts

    def set_value(self, value):
        self.value = value
        if (len(self.fanouts)):
            for fanout in self.fanouts:
                self.fanouts[fanout].value = self.value
        return self.value