from .node import Node

class Gate:
    def __init__(self, name: str = '', type: str = '', inputs: list = [Node], output = Node):
        self.name = name
        self.type = type
        self.inputs = inputs
        self.output = output
        self.no_inputs = self.__get_number_of_inputs

    def __get_number_of_inputs(self):
        return len(self.inputs)

class AND(Gate):
    def calculate(self):
        return self.output.set_value(int(self.inputs[0].value and self.inputs[1].value))

class OR(Gate):
    def calculate(self):
        return self.output.set_value(int(self.inputs[0].value or self.inputs[1].value))

class NOT(Gate):
    def calculate(self, input):
        return self.output.set_value(int(not input.value))

class XOR(Gate):
    def calculate(self):
        return self.output.set_value(int((not self.inputs[0].value and self.inputs[1].value) or (self.inputs[0].value and not self.inputs[1].value)))

class NAND(Gate):
    def calculate(self):
        return self.output.set_value(int(not (self.inputs[0].value and self.inputs[1].value)))

class NOR(Gate):
    def calculate(self):
        return self.output.set_value(int(not (self.inputs[0].value or self.inputs[1].value)))

class XNOR(Gate):
    def calculate(self):
        return self.output.set_value(int((not self.inputs[0].value and not self.inputs[1].value) or (self.inputs[0].value and self.inputs[1].value)))
