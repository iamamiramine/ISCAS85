from components import circuit, node, parse
from components import gate as g_

if __name__ == "__main__":
    # input1 = node.Node(type=0, value=0)
    # input2 = node.Node(type=0, value=0)
    # input3 = node.Node(type=0, value=0)
    # input4 = node.Node(type=0, value=0)
    # output1 = node.Node(1)
    # xor2 = gate.NOR(name="XNOR2", type="XNOR", inputs=[input1, input2], output=output1)
    # xor2.calculate()

    # print(xor2.type)
    # print(xor2.output.value)

    parser = parse.Parser("circuits/c17.txt")
    c17 = parser.parse_iscas85()

    print("Circuit name: " + c17.name)

    print("Primary Inputs: ")
    for pi in c17.pi:
        print("Input name: " + str(c17.pi[pi].name) + ", Input value: " + str(c17.pi[pi].value) + ", Fanouts: " + str(c17.pi[pi].fanouts))

    print("Primary Outputs: ")
    for po in c17.po:
        print("Output name: " + str(c17.po[po].name) + ", Output value: " + str(c17.po[po].value))

    print("Gates: ")
    for gate in c17.gates:
        g = c17.gates[gate]
        print(" Gate: " + g.name, g.inputs, g.output)

    # print(parser.list_outputs[11].fanouts)

    c17.simulate()
    # TODO:
    # create a file system for input vectors for each circuit
    # store the output results for comparison
    # implement concurrent fault simulation