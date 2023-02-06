# ucsbcs154lab4
# All Rights Reserved
# Copyright (c) 2023 Regents of the University of California
# Distribution Prohibited

import pyrtl

# instantiate a memory block that has our sample instructions stored in it 
# translate the following instructions from decimal to MIPS assembly and place in decoded.txt for part 1 (c)
sample_instructions = [287965187, 201326593, 2381053956, 6301728]
mem = pyrtl.RomBlock(bitwidth=32, addrwidth=2, romdata=sample_instructions, max_read_ports=1)

# variable counter will serve as an address in this example 
counter = pyrtl.Register(bitwidth=2, name='counter')
counter.next <<= counter + 1

# read data stored in rom
data = pyrtl.WireVector(bitwidth=32, name='data')
data <<= mem[counter]

# output data
#op = pyrtl.Output(bitwidth=<add your code here>, name='op')
#rs = pyrtl.Output(bitwidth=<add your code here>, name='rs')
#rt = pyrtl.Output(bitwidth=<add your code here>, name='rt')
#rd = pyrtl.Output(bitwidth=<add your code here>, name='rd')
#sh = pyrtl.Output(bitwidth=<add your code here>, name='sh')
#func = pyrtl.Output(bitwidth=<add your code here>, name='func')
#imm = pyrtl.Output(bitwidth=<add your code here>, name='imm')
#addr = pyrtl.Output(bitwidth=<add your code here>, name='addr')

### ADD YOUR INSTRUCTION DECODE LOGIC HERE ###

# simulate
sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)
for cycle in range(4):
    sim.step({})
sim_trace.render_trace(symbol_len=20, segment_size=1)
