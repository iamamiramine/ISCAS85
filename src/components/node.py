class Node:

    def __init__(self, name: int = 0, type: int = 0, value: int = 0, fanouts: list = []):
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