class Circuit:

    def __init__(self, name: str = '', gates: dict = {}, pi: dict = {}, po: dict = {}):
        self.name = name
        self.gates = gates
        self.pi = pi
        self.po = po