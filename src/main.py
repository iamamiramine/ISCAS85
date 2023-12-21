import time

from components import circuit, node, parse
from components import gate as g_
import serial_algorithm

def print_results():
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
    start_time = time.time()
    parser = parse.Parser("circuits/c17.txt")
    c17 = parser.parse_iscas85()
    end_time_parse = time.time()
    run_time_parse = end_time_parse - start_time
    print(f"Parse Run Time: {run_time_parse} seconds")

    fault_coverage, test_vectors_faults, fault_efficiency = serial_algorithm.run_serial(c17, 'inputs/c17_input.txt')
    print("Fault Coverage: ", fault_coverage)
    print("Test Vectors Faults: ", test_vectors_faults)
    print("Fault Efficiency: ", fault_efficiency)
    end_time = time.time()
    run_time = end_time - start_time
    print(f"Total Run Time: {run_time} seconds")