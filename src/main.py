from components import circuit, node, parse
from components import gate as g_
import serial

def print(results):
    # print("Circuit name: " + c17.name)

    # print("Primary Inputs: ")
    # for pi in c17.pi:
    #     print("Input name: " + str(c17.pi[pi].name) + ", Input value: " + str(c17.pi[pi].value) + ", Fanouts: " + str(c17.pi[pi].fanouts))

    # print("Primary Outputs: ")
    # for po in c17.po:
    #     print("Output name: " + str(c17.po[po].name) + ", Output value: " + str(c17.po[po].value))

    # print("Gates: ")
    # for gate in c17.gates:
    #     g = c17.gates[gate]
    #     print(" Gate: " + g.name, g.inputs, g.output)
    return

if __name__ == "__main__":
    parser = parse.Parser("circuits/c17.txt")
    c17 = parser.parse_iscas85()

    fault_coverage, test_vectors_faults, remianing_faults = serial.run_serial(c17, 'inputs/c17_input.txt')