from components.circuit import Circuit
from components import node, gate

class Parser:
    def parse_iscas85(file_name):
        """Parse ISCAS-85 netlist file and return a structured format."""
        
        with open(file_name, 'r') as file:
            lines = file.readlines()
            
        circuit_name = lines[0][2:]
        no_inputs = int(lines[1][2])
        no_outputs = int(lines[2][2])
        no_not = int(lines[3][2])
        gates = lines[4][12:-3]

        gates = gates.split(" + ")

        list_inputs = []
        list_outputs = []

        # Inputs
        for i in range(7, no_inputs+6):
            pi = node.Node(name=int(lines[i][-3]), type=0)
            list_inputs.append(pi)

        print(list_inputs)

        
        # NOT Gate
        if no_not != 0:
            for i in range(0, no_not):
                print("")
                # Create NOT gates

        for gate in gates:
            no_gates = gate[0]
            gate_type = gate[2:-1] if gate[-1] == "s" else gate[2:]
            

        
        # # Loop through the lines to parse the information
        # for line in lines:
        #     line = line.strip()
            
        #     if line.startswith("#") or len(line) == 0:
        #         # Skip comments and empty lines
        #         continue
            
        #     parts = line.split(" ")
        #     gate_type = parts[0]
            
        #     # Depending on the type of the gate, we'll parse differently
        #     if gate_type == "INPUT":
        #         # Example: INPUT(1)
        #         node_name = parts[1][6:-1]
        #         circuit[node_name] = {"type": "INPUT", "outputs": []}
        #     elif gate_type == "OUTPUT":
        #         # Example: OUTPUT(23)
        #         node_name = parts[1][7:-1]
        #         circuit[node_name] = {"type": "OUTPUT", "inputs": []}
        #     else:
        #         # Example: 10 = AND(6, 7)
        #         output_node = parts[0]
        #         inputs = [inp.strip("(),") for inp in parts[2:]]
        #         circuit[output_node] = {"type": gate_type, "inputs": inputs, "outputs": []}
                
        #         # Populate the output information for the input nodes
        #         for inp in inputs:
        #             if inp not in circuit:
        #                 circuit[inp] = {"type": None, "inputs": [], "outputs": []}
        #             circuit[inp]["outputs"].append(output_node)
                    
        # return circuit

if __name__ == "_main__":
    Parser.parse_iscas85("circuits/c17.txt")
        
