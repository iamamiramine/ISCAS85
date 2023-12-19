class Circuit:

    def __init__(self, name: str = '', gates: dict = {}, pi: dict = {}, list_outputs: dict = {}, list_fanouts:dict = {}, po: dict = {}, max_turns: int = 1):
        self.name = name
        self.gates = gates
        self.pi = pi
        self.list_outputs = list_outputs
        self.list_fanouts = list_fanouts
        self.po = po
        self.max_turns = max_turns

    def simulate(self, test_vector: list = []):
        keys = list(self.pi.keys())
        # Set PI values
        for i, key in enumerate(keys):
            if self.pi[key].faulty:
                self.pi[key].set_value(self.pi[key].fault)
            else:
                self.pi[key].set_value(test_vector[i])
            if len(self.pi[key].fanouts):
                for f in self.pi[key].fanouts:
                    fanout = self.pi[key].fanouts[f]
                    fanout.set_value(self.pi[key].value)
                    # print(fanout.name)
                    # print(fanout.value)


        # Simulate
        for gate_counter in range(1, self.max_turns+1):
            for gate in self.gates:
                g = self.gates[gate]
                if g.turn == gate_counter:
                    # print("TURN: " + str(g.name))
                    for inp in g.inputs:
                        if g.inputs[inp].faulty:
                            g.inputs[inp].set_value(g.inputs[inp].fault)
                        # print("Input: " + str(g.inputs[inp].name), str(g.inputs[inp].value), str(g.inputs[inp].fault))
                    if g.output.faulty:
                        g.output.set_value(g.fault)
                        if len(g.output.fanouts):
                            for f in g.output.fanouts:
                                fanout = g.output.fanouts[f]
                                fanout.set_value(g.output.value)
                    else:
                        g.calculate()
                    # print(g.output.name)
                    # print(g.output.value)

    def fault_simulation(self, fault_site: dict = {}):
        pi_keys = list(self.pi.keys())
        po_keys = list(self.po.keys())
        lo_keys = list(self.list_outputs.keys())
        fo_keys = list(self.list_fanouts.keys())

        # Fault Injection
        for i, key in enumerate(pi_keys):
            if self.pi[key].name in fault_site:
                self.pi[key].faulty = True
                self.pi[key].fault = fault_site[self.pi[key].name]
                self.pi[key].set_value(fault_site[self.pi[key].name])

        for i, key in enumerate(lo_keys):
            if self.list_outputs[key].name in fault_site:
                self.list_outputs[key].faulty = True
                self.list_outputs[key].fault = fault_site[self.list_outputs[key].name]
                self.list_outputs[key].set_value(fault_site[self.list_outputs[key].name])     

        for i, key in enumerate(fo_keys):
            if self.list_fanouts[key].name in fault_site:
                self.list_fanouts[key].faulty = True
                self.list_fanouts[key].fault = fault_site[self.list_fanouts[key].name]
                self.list_fanouts[key].set_value(fault_site[self.list_fanouts[key].name])   

        for i, key in enumerate(po_keys):
            if self.po[key].name in fault_site:
                self.po[key].faulty = True
                self.po[key].fault = fault_site[self.po[key].name]
                self.po[key].set_value(fault_site[self.po[key].name]) 