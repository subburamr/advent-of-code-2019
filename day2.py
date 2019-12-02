def read_intcode():
    input = open("data/day2_input.txt").read()
    orig_intcode_vals = list(map(int, input.split(',')))
    return orig_intcode_vals

start_pos = 0
jump = 4

def transform_opcode(intcode_vals):
    """Convert given opcode into transformed op code

    Parameters
    ----------
    opcode : [List]
        List of ints

    Returns
    -------
    [List]
        List of ints
    """
    for i in range(start_pos, len(intcode_vals), jump):
        opcode = intcode_vals[i]
        if opcode == 1:
            intcode_vals[intcode_vals[i+3]] = intcode_vals[intcode_vals[i+1]] +  intcode_vals[intcode_vals[i+2]]
        elif opcode == 2:
            intcode_vals[intcode_vals[i+3]] = intcode_vals[intcode_vals[i+1]] *  intcode_vals[intcode_vals[i+2]]
        elif opcode == 99:
           break
    return intcode_vals

assert transform_opcode([1,0,0,0,99]) == [2,0,0,0,99]
assert transform_opcode([2,3,0,3,99]) == [2,3,0,6,99]
assert transform_opcode([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
assert transform_opcode([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]

import itertools as it

for noun, verb in it.product(range(100), repeat=2):
    curr_intcode_vals = read_intcode()
    # curr_intcode_vals = orig_intcode_vals
    curr_intcode_vals[1] = noun
    curr_intcode_vals[2] = verb
    if transform_opcode(curr_intcode_vals)[0] ==  19690720:
        print(noun * 100 + verb)
        break
