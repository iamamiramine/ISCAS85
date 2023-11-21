from components import circuit, gate, node, parse

if __name__ == "__main__":
    # input1 = node.Node(type=0, value=0)
    # input2 = node.Node(type=0, value=0)
    # output1 = node.Node(1)
    # xor2 = gate.NOR(name="XNOR2", type="XNOR", inputs=[input1, input2], output=output1)
    # xor2.calculate()

    # print(xor2.type)
    # print(xor2.output.value)

    parser = parse.Parser
    parser.parse_iscas85("circuits/c17.txt")
