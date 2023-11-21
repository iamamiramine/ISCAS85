class Circuit:

    def __init__(self, name: str = '', gates: dict = {}, pi: dict = {}, po: dict = {}, max_turns: int = 1):
        self.name = name
        self.gates = gates
        self.pi = pi
        self.po = po
        self.max_turns = max_turns

    def simulate(self, test_vector: list = []):
        test_vector = [0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1]
        keys = list(self.pi.keys())
        for i, key in enumerate(keys):
            self.pi[key].set_value(test_vector[i])

        for gate_counter in range(1, self.max_turns+1):
            for gate in self.gates:
                g = self.gates[gate]
                if g.turn == gate_counter:
                    # print("LEVEL: " + str(gate_counter))
                    g.calculate()
                    # print(g.output.name)
                    # print(g.output.value)