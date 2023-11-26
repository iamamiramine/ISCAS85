import re

from components.circuit import Circuit
from components import node
from components import gate as g_

class Parser:
    def __init__(self, file_path):
        self.file_path = file_path  # circuit file path
        self.list_gates = {}    # list of circuit gates
        self.pi = {}    # list of primary inputs
        self.po = {}    # list of primary outputs
        self.list_outputs = {}  # list of middle circuit outputs

    def parse_iscas85(self):
        """Parse ISCAS-85 netlist file and return a structured format."""

        def _test(self):
            '''TEST'''

            for i in self.list_inputs:
                print(self.list_inputs[i].name)

            for i in self.list_outputs:
                print(self.list_outputs[i].name)

            print(self.list_gates)
            for nand in self.list_gates["NAND"]:
                # Inputs
                print("Input")
                for inp in nand.inputs:
                    print(inp.name)
                # Output
                print("Output")
                print(nand.output.name)
        
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            
        ''' Header '''
        circuit_name = lines[0][2:]
        no_inputs = int(re.search(r'\d+', lines[1]).group())    # number of inputs
        no_outputs = int(re.search(r'\d+', lines[2]).group())   # number of outputs
        no_not = int(re.search(r'\d+', lines[3]).group())       # number of inverters
        no_gates = int(re.search(r'\d+', lines[4]).group())     # number of gates
        # not used
        gates = lines[4][12:-3]
        gates = gates.split(" + ")

        '''Inputs'''
        # Create an instance of each input and add it to the list of primary inputs
        input_max_line = 6+no_inputs
        for i in range(6, input_max_line):
            name = int(re.search(r'\d+', lines[i]).group())
            pi = node.Node(name=name, type=0)
            self.pi[name] = pi

        ''' Outputs '''
        # Create an instance of each output and add it to the list of primary outputs
        output_max_line = input_max_line+1+no_outputs
        for i in range(input_max_line+1, output_max_line):
            name = int(re.search(r'\d+', lines[i]).group())
            po = node.Node(name=name, type=1)
            self.po[name] = po

        ''' Gates '''
        # counting instances of each gate
        gate_counters = {
            "NAND": 1,
            "NOT": 1,
            "NOR": 1,
            "XNOR": 1,
            "XOR": 1,
            "AND": 1,
            "OR": 1
        }

        gate_turn = 1
        input_counter={}
        gate_max_line = output_max_line+1+no_gates+no_not
        for i in range(output_max_line+1, gate_max_line):
            gate = " ".join(re.findall("[a-zA-Z]+", lines[i]))  # get gate type
            in_out = re.findall('\d+', lines[i])    # get gate inputs and outputs

            # gate specific initialization
            gate_input_list = {}    # dictionary of gate specific input
            gate_output_list = {}   # dictionary of gate specific output

            # Checks if output already exists
            # in the list of primary outputs
            outp = int(in_out[0])
            if (outp) in self.po:
                gate_output = self.po[outp]
                gate_output_list[outp] = gate_output
            else: # Create new middle circuit output
                gate_output = node.Node(name=outp, type = 1)
                self.list_outputs[outp] = gate_output
                gate_output_list[outp] = gate_output

            # iterate over gate inputs
            for inp in in_out[1:]:
                inp = int(inp)
                # check if input has fanouts
                if inp in input_counter:
                    input_counter[inp] += 1
                else:
                    input_counter[inp] = 1

            for inp in in_out[1:]:
                # Checks if input already exists
                # in the list of primary inputs
                if inp in self.pi:
                    gate_input_list[inp] = self.pi[inp]
                # Checks if input already exists
                # in the list of middle circuit outputs
                elif inp in self.list_outputs: # output of a gate can be an input of another
                    gate_input_list[inp] = self.list_outputs[inp]
                    gate_turn+=1        # increment gate turn whenever it needs an input which depends on the output of another gate
                else:
                    print("ERROR")      # not possible since gate input either exists as a primary input or as another gate output
                                        # cannot initialize input as a new input if it does not already exists as one of the two above states

            # Create gate instances
            if(gate=="AND"):
                gate_name = gate + str(gate_counters[gate])
                gate_counters[gate] +=1
                self.list_gates[gate_name] = g_.AND(name = gate_name, type=gate, inputs=gate_input_list, output=gate_output, turn=gate_turn)
            elif(gate=="OR"):
                gate_name = gate + str(gate_counters[gate])
                gate_counters[gate] +=1
                self.list_gates[gate_name] = g_.OR(name = gate_name, type=gate, inputs=gate_input_list, output=gate_output, turn=gate_turn)
            elif(gate=="NOT"):
                gate_name = gate + str(gate_counters[gate])
                gate_counters[gate] +=1
                self.list_gates[gate_name] = g_.NOT(name = gate_name, type=gate, inputs=gate_input_list, output=gate_output, turn=gate_turn)
            elif(gate=="XOR"):
                gate_name = gate + str(gate_counters[gate])
                gate_counters[gate] +=1
                self.list_gates[gate_name] = g_.XOR(name = gate_name, type=gate, inputs=gate_input_list, output=gate_output, turn=gate_turn)
            elif(gate=="NAND"):
                gate_name = gate + str(gate_counters[gate])
                gate_counters[gate] +=1
                self.list_gates[gate_name] = g_.NAND(name = gate_name, type=gate, inputs=gate_input_list, output=gate_output, turn=gate_turn)
            elif(gate=="NOR"):
                gate_name = gate + str(gate_counters[gate])
                gate_counters[gate] +=1
                self.list_gates[gate_name] = g_.NOR(name = gate_name, type=gate, inputs=gate_input_list, output=gate_output, turn=gate_turn)
            elif(gate=="XNOR"):
                gate_name = gate + str(gate_counters[gate])
                gate_counters[gate] +=1
                self.list_gates[gate_name] = g_.XNOR(name = gate_name, type=gate, inputs=gate_input_list, output=gate_output, turn=gate_turn)

        # Create circuit instance
        circuit = Circuit(name=circuit_name, gates=self.list_gates, pi = self.pi, po = self.po, max_turns=gate_turn)

        return circuit

if __name__ == "_main__":
    Parser.parse_iscas85("circuits/c17.txt")