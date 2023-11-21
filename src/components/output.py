from fanouts import FanOut

class Output:

    def __init__(self, num = 0, fanout = FanOut):
        self.num = num
        self.fanout = fanout
        self.value = None

    def set_value(self, value):
        self.value = value