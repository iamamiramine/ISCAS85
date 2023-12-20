import re

from components.circuit import Circuit as C_
from components import node, parse

def run_serial(circuit: C_, input_file: str='inputs/c17_inputs.txt'):
    '''
        Run Serial Algorithm
            Detects:
                Single Stuck at Faults
                Multiple Stuck at Faults
            Does not detect:
                Redundant faults
    '''
    # Parse Test Input file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    '''Header'''
    no_input_vectors = int(re.search(r'\d+', lines[1]).group())    # number of input vectors
    no_saf = int(re.search(r'\d+', lines[2]).group())   # number of stuck at faults

    '''Initialize'''
    test_vectors_faults = {}    # Test Vectors with the faults that each vector detected
    faults = []     # Circuit Faults. We will remove from this list the detected faults.
    test_vector_max_lines = 5+no_input_vectors      # For reading Input Vector from file
    saf_max_line = test_vector_max_lines+2+no_saf   # For reading Stuck-at-faults from file
    fault_count = 0     # Fault count for detected faults. This will be used to calculate fault coverage

    '''Add Faults'''
    for j in range(test_vector_max_lines+2, saf_max_line):
                fault = re.findall('\d+\.\d+|\d+', lines[j])
                fault_site = {
                    float(fault[0]): int(fault[1])
                }
                faults.append(fault_site)   # Adding faults from input file to dictionary

    '''Serial'''
    for i in range(5, test_vector_max_lines): # Iterating through the test vectors
        test_vector = re.findall('\d+', lines[i]) # Read test vector
        test_vector_str = "".join(test_vector) # Convert test vector from list to string (if we used the test vector as a string immediately from text file, it will be in the form of '0,0,0,1,1\n')
        test_vectors_faults[test_vector_str] = [] # Add test vector to dictionary
        true_value = {} # For comparing true value simulation with faulty simulation
        detected_faults = [] # List of detected faults for each test vector

        '''True Value Simulation'''
        circuit.simulate(test_vector)               
        for k in circuit.po:
            true_value[circuit.po[k]] = circuit.po[k].value # Save the true values
            # print(circuit.po[k].name, circuit.po[k].value) # Print True Value Outputs

        '''Fault Simulation'''
        for fault in faults:                  
            fault_site = fault # stuck at fault
            circuit.fault_injection(fault_site) # Inject Fault
            circuit.simulate(test_vector) # Fault Simulation

            '''Comparing true value simulation with faulty simulation'''
            Detected = False # Flag to check if fault is detected
            for k in circuit.po:
                if circuit.po[k].value != true_value[circuit.po[k]]: # If Faulty simualtion output is different than true value simulation
                    Detected = True # Fault is detected
                    # print(circuit.po[k].name, circuit.po[k].value) # Print Faulty Outputs
                    
            if Detected: # Fault is detected
                test_vectors_faults[test_vector_str].append(fault_site) # Associate the fault with the test vector that detected it
                detected_faults.append(fault_site) # Add fault to detected fault list
                fault_count += 1 # Increment detected faults count

        for detected_fault in detected_faults: # Iterate over detected faults to remove from main faults dictionary so that we do not test them for other test vectors
            faults.remove(detected_fault)
 
    fault_coverage = fault_count/no_saf # Fault Coverage

    return fault_coverage, test_vectors_faults, faults # Returns fault coverage, test vectors with the faults it detected, and undetectable faults