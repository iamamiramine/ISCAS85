class Circuit:

    def __init__(self, name: str = '', gates: list = [], pi: list = [], po: list = [], fanouts: list = []):
        self.name = name
        self.gates = gates
        self.pi = pi
        self.po = po
        self.fanouts = fanouts