from .node import Node

class Gate:
    def __init__(self, name: str = '', type: str = '', inputs: dict = {}, output = Node, turn: int = 1):
        self.name = name
        self.type = type
        self.inputs = inputs
        self.output = output    # a gate has one output only
        self.no_inputs = self.__get_number_of_inputs
        self.turn = turn    # turn is when the gate will be simulated (at which iteration)

    def __get_number_of_inputs(self):
        return len(self.inputs)

class AND(Gate):
    def calculate(self):
        input_values = []
        for inp in self.inputs:
            input_values.append(self.inputs[inp].value)
        return self.output.set_value(int (all(i == 1 for i in input_values)))

class OR(Gate):
    def calculate(self):
        input_values = []
        for inp in self.inputs:
            input_values.append(self.inputs[inp].value)
        return self.output.set_value(int (any(i == 1 for i in input_values)))

class NOT(Gate):
    '''NOT gate has 1 input only'''
    def calculate(self):
        return self.output.set_value(int(not self.inputs[list(self.inputs.keys())[0]].value))

class XOR(Gate):
    '''For ISCAS85 Bench Circuits, there are no XORs with more than 2 inputs'''
    def calculate(self):
        return self.output.set_value(int((not self.inputs[list(self.inputs.keys())[0]].value and self.inputs[list(self.inputs.keys())[1]].value) 
                                            or (self.inputs[list(self.inputs.keys())[0]].value and not self.inputs[list(self.inputs.keys())[1]].value)))

class NAND(Gate):
    def calculate(self):
        input_values = []
        for inp in self.inputs:
            input_values.append(self.inputs[inp].value)
        return self.output.set_value(int(not (all(i == 1 for i in input_values))))

class NOR(Gate):
    def calculate(self):
        input_values = []
        for inp in self.inputs:
            input_values.append(self.inputs[inp].value)
        return self.output.set_value(int(not (any(i == 1 for i in input_values))))

class XNOR(Gate):
    '''For ISCAS85 Bench Circuits, there are no XNOR gates'''
    def calculate(self):
        return self.output.set_value(int((not self.inputs[list(self.inputs.keys())[0]].value and not self.inputs[list(self.inputs.keys())[1]].value) 
                                         or (self.inputs[list(self.inputs.keys())[0]].value and self.inputs[list(self.inputs.keys())[1]].value)))
