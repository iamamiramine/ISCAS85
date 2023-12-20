from .node import Node

class Gate:
    '''
        Gate Class
            This class represents:
                AND
                OR
                NOT
                NAND
                NOR
                XOR
                XNOR
                BUFFER
            Each Child Gate Subclass extends attributes from Base Gate Class
            Each Gate Class hass a calculate method which calculates output based on input values.
            All Gates can have two or more inputs except for:
                XOR
                XNOR
                NOT
                BUFFER
    '''
    def __init__(self, name: str = '', type: str = '', inputs: dict = {}, output = Node, turn: int = 1):
        self.name = name
        self.type = type
        self.inputs = inputs # Dictionary of Nodes, which are inputs to the gate
        self.output = output    # a gate has one output only
        self.no_inputs = self.__get_number_of_inputs
        self.turn = turn    # turn is when the gate will be simulated (at which iteration). This is to make sure gate inputs stabalize before calculating the gate outpu

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
    
class BUFF(Gate):
    '''Buffer gate has 1 input only'''
    def calculate(self):
        return self.output.set_value(int(self.inputs[list(self.inputs.keys())[0]].value))

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
