import re

from components.circuit import Circuit
from components import node
from components import gate as g_

class Parser:
    def __init__(self, file_name):
        self.file_name = file_name
        self.list_gates = {}
        self.list_inputs = {}
        self.list_outputs = {}
        self.pi = {}
        self.po = {}

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
        
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
            
        circuit_name = lines[0][2:]
        no_inputs = int(re.search(r'\d+', lines[1]).group())
        no_outputs = int(re.search(r'\d+', lines[2]).group())
        no_not = int(re.search(r'\d+', lines[3]).group())
        no_gates = int(re.search(r'\d+', lines[4]).group())
        gates = lines[4][12:-3]

        gates = gates.split(" + ")
        for gate in gates:
            gate = " ".join(re.findall("[a-zA-Z]+", gate))
            gate_type = gate[:-1] if gate[-1] == "s" else gate
            self.list_gates[gate_type] = []

        # Inputs
        for i in range(6, 6+no_inputs):
            name = int(re.search(r'\d+', lines[i]).group())
            pi = node.Node(name=name, type=0)
            self.list_inputs[name] = pi
            self.pi[name] = pi

        # Outputs
        for i in range(6+no_inputs+1, 6+no_inputs+1+no_outputs):
            name = int(re.search(r'\d+', lines[i]).group())
            po = node.Node(name=name, type=1)
            self.list_outputs[name] = po
            self.po[name] = po

        gate_counters = {
            "NAND": 1,
            "NOT": 1,
            "NOR": 1,
            "XNOR": 1,
            "XOR": 1,
            "AND": 1,
            "OR": 1
        }

        for i in range(6+no_inputs+1+no_outputs+1, 6+no_inputs+1+no_outputs+1+no_gates+no_not):
            # print(lines[i].split())
            gate = " ".join(re.findall("[a-zA-Z]+", lines[i]))
            in_out = re.findall('\d+', lines[i])
            gate_input_list = {}
            gate_output_list = {}

            if in_out[1] in self.list_inputs:    # Check if first input is in list of inputs
                gate_input_list[in_out[1]] = self.list_inputs[in_out[1]]
            elif in_out[1] in self.list_outputs: # Check if first input is in list of outputs
                gate_input_list[in_out[1]] = self.list_outputs[in_out[1]]
            else:   # Create a new input (this else is usually not called since the middle circuit output is created in the list of outputs)
                gate_new_input = node.Node(name=in_out[1], type = 0)
                gate_input_list[in_out[1]] = gate_new_input

            if in_out[2] in self.list_inputs:    # Check if second input is in list of inputs
                gate_input_list[in_out[2]] = self.list_inputs[in_out[2]]
            elif in_out[2] in self.list_outputs: # Check if second input is in list of outputs
                gate_input_list[in_out[2]] = self.list_outputs[in_out[2]]
            else:   # Create a new input (this else is usually not called since the middle circuit output is created in the list of outputs)
                gate_new_input = node.Node(name=in_out[2], type = 0)
                gate_input_list[in_out[2]] = gate_new_input

            # Check if output already exists
            if (in_out[0]) in self.list_outputs:
                gate_output = self.list_outputs[in_out[0]]
                gate_input_list[in_out[0]] = gate_output
            else: # Create new middle circuit output
                gate_output = node.Node(name=in_out[0], type = 1)
                gate_input_list[in_out[0]] = gate_output

            if(gate=="AND"):
                gate_name = gate + str(gate_counters[gate])
                gate_counters[gate] +=1
                self.list_gates[gate].append(g_.AND(name = gate_name, type=gate, inputs=gate_input_list, output=gate_output))
            elif(gate=="OR"):
                gate_name = gate + str(gate_counters[gate])
                gate_counters[gate] +=1
                self.list_gates[gate].append(g_.OR(name = gate_name, type=gate, inputs=gate_input_list, output=gate_output))
            elif(gate=="NOT"):
                gate_name = gate + str(gate_counters[gate])
                gate_counters[gate] +=1
                self.list_gates[gate].append(g_.NOT(name = gate_name, type=gate, inputs=gate_input_list, output=gate_output))
            elif(gate=="XOR"):
                gate_name = gate + str(gate_counters[gate])
                gate_counters[gate] +=1
                self.list_gates[gate].append(g_.XOR(name = gate_name, type=gate, inputs=gate_input_list, output=gate_output))
            elif(gate=="NAND"):
                gate_name = gate + str(gate_counters[gate])
                gate_counters[gate] +=1
                self.list_gates[gate].append(g_.NAND(name = gate_name, type=gate, inputs=gate_input_list, output=gate_output))
            elif(gate=="NOR"):
                gate_name = gate + str(gate_counters[gate])
                gate_counters[gate] +=1
                self.list_gates[gate].append(g_.NOR(name = gate_name, type=gate, inputs=gate_input_list, output=gate_output))
            elif(gate=="XNOR"):
                gate_name = gate + str(gate_counters[gate])
                gate_counters[gate] +=1
                self.list_gates[gate].append(g_.XNOR(name = gate_name, type=gate, inputs=gate_input_list, output=gate_output))

        circuit = Circuit(name=circuit_name, gates=self.list_gates, pi = self.pi, po = self.po)

        return circuit

if __name__ == "_main__":
    Parser.parse_iscas85("circuits/c17.txt")