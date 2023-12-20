class Circuit:

    def __init__(self, name: str = '', gates: dict = {}, pi: dict = {}, list_outputs: dict = {}, list_fanouts:dict = {}, po: dict = {}, max_turns: int = 1):
        self.name = name
        self.gates = gates
        self.pi = pi
        self.list_outputs = list_outputs
        self.list_fanouts = list_fanouts
        self.po = po
        self.max_turns = max_turns # Number of iterations to simulate a circuit

    def simulate(self, test_vector: list = []):
        keys = list(self.pi.keys())
        
        '''Set Primary Inputs Values'''
        for i, key in enumerate(keys):
            if self.pi[key].faulty: # Check if PI is faulty
                self.pi[key].set_value(self.pi[key].fault) # Set PI to fault value
            else:
                self.pi[key].set_value(int(test_vector[i])) # Set PI to value from test vector
            if len(self.pi[key].fanouts): # IF PI has fanouts
                for f in self.pi[key].fanouts: # Set fanout branches values to stem value
                    fanout = self.pi[key].fanouts[f]
                    fanout.set_value(self.pi[key].value)

        # Simulate
        for gate_counter in range(1, self.max_turns+1):
            for gate in self.gates:
                g = self.gates[gate] # get the gate attributes
                if g.turn == gate_counter: # If the gate should be simulated at this iteration
                    for inp in g.inputs: # Iterate through gate inputs
                        if g.inputs[inp].faulty: # check if gate input is faulty
                            g.inputs[inp].set_value(g.inputs[inp].fault) # assign gate input to fault value
                    if g.output.faulty: # if gate output is faulty
                        g.output.set_value(g.output.fault) # Discard gate output calculation and assign gate output to the fault value
                        if len(g.output.fanouts): # if gate output has fanouts
                            for f in g.output.fanouts:
                                fanout = g.output.fanouts[f]
                                fanout.set_value(g.output.value) # assign fanout value to gate output value
                    else: # Assign gate output based on gate output calculation
                        g.calculate()

    def fault_injection(self, fault_site: dict = {}):
        '''Inject faults at fault site'''

        # Get Primary Inputs, Outputs and Fanouts
        pi_keys = list(self.pi.keys())
        po_keys = list(self.po.keys())
        lo_keys = list(self.list_outputs.keys())
        fo_keys = list(self.list_fanouts.keys())

        # Fault Injection
        for i, key in enumerate(pi_keys):
            if self.pi[key].name in fault_site: # Check if fault is to be injected at PI
                self.pi[key].faulty = True
                self.pi[key].fault = fault_site[self.pi[key].name]
                self.pi[key].set_value(fault_site[self.pi[key].name])

        for i, key in enumerate(lo_keys):
            if self.list_outputs[key].name in fault_site: # Check if fault is to be injected at gate output and fanout stems
                self.list_outputs[key].faulty = True
                self.list_outputs[key].fault = fault_site[self.list_outputs[key].name]
                self.list_outputs[key].set_value(fault_site[self.list_outputs[key].name])     

        for i, key in enumerate(fo_keys):
            if self.list_fanouts[key].name in fault_site: # Check if fault is to be injected at fanout branches
                self.list_fanouts[key].faulty = True
                self.list_fanouts[key].fault = fault_site[self.list_fanouts[key].name]
                self.list_fanouts[key].set_value(fault_site[self.list_fanouts[key].name])   

        for i, key in enumerate(po_keys):
            if self.po[key].name in fault_site: # Check if fault is to be injected at primary output
                self.po[key].faulty = True
                self.po[key].fault = fault_site[self.po[key].name]
                self.po[key].set_value(fault_site[self.po[key].name]) 