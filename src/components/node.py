class Node:
    '''
        Node Class
            This class represents the inputs, outputs, and fanouts
    '''
    def __init__(self, name: float = 0.0, type: int = 0, value: int = 0, fanouts: dict = {}, faulty: bool = False, fault: int = 0):
        self.name = name # Node name (i.e. 1, 3.1, 16)
        self.type = type # Node type (0 for input, 1 for output)
        self.value = value # Node value (0 or 1)
        self.fanouts = fanouts # Dictionary of node fanouts
        self.faulty = faulty # Boolean, whether node is faulty
        self.fault = None # fault type (sa0 or sa1)

    def set_value(self, value):
        '''Set Value
            Sets Node value during simulation
            Example:
                during AND.calculate()
                    AND.output.set_value(input[0] and input[1])
                during true value simulation: set the primary inputs to the test vector value
                    test_vector = [0,0,1]
                    pi_1.set_value(0)
                    pi_2.set_value(0)
                    pi_3.set_value(1)
        '''
        self.value = value
        if (len(self.fanouts)): # if node has fanouts
            for fanout in self.fanouts:
                self.fanouts[fanout].value = self.value # set fanout branches values to fanout stem value
        return self.value