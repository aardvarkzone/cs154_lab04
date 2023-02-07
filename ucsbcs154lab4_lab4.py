import pyrtl
# r type: ADD, SUB, AND, OR, XOR, SLL, SRL, SRA, and SLT
    # need to look at func to find which one
    # ADD: 100000
    # SUB: 100010
    # AND: 100100
    # OR: 100101
    # XOR: 100110
    # SLL: 000000
    # SRL: 000010
    # SRA: 000011
    # SLT: 101010

# 32 registers in register file part of data path
# memblock to implement register file called rf 
# 

rf = pyrtl.MemBlock(bitwidth=32, addrwidth=5, 
                    name='rf', max_read_ports=2,
                    max_write_ports=1)

instr = pyrtl.Input(bitwidth=32, name='instr')
alu_out = pyrtl.WireVector(bitwidth=32, name='alu_out')
rs = pyrtl.WireVector(bitwidth=5, name='rs')
rt = pyrtl.WireVector(bitwidth=5, name='rt')
rd = pyrtl.WireVector(bitwidth=5, name='rd')
sh = pyrtl.WireVector(bitwidth=5, name='sh')
func = pyrtl.WireVector(bitwidth=6, name='func')

rs <<= instr[21:26]
rt <<= instr[16:21]
rd <<= instr[11:16]
sh <<= instr[6:11]
func <<= instr[0:6]

#r_reg0 = pyrtl.WireVector(bitwidth=5, name='read regsiter 0 (rs)')
#r_reg1 = pyrtl.WireVector(bitwidth=5, name='read regsiter 1 (rt)')
data0 = pyrtl.WireVector(bitwidth=5, name='data 0')
data1 = pyrtl.WireVector(bitwidth=5, name='data 1')
#w_reg = pyrtl.WireVector(bitwidth=5, name='write register (rd)' )

#r_reg0 <<= rs
#r_reg1 <<= rt
data0 <<= rf[rs]
data1 <<= rf[rt]

with pyrtl.conditional_assignment:
    with func == 0b100000:
        #ADD
        alu_out |= (data0 + data1)
    with func == 0b100010:
        #SUB
        alu_out |= (data0 - data1)
    with func == 0b100100:
        #AND
        alu_out |= (data0 & data1)
    with func == 0b100101:
        #OR
        alu_out |= (data0 | data1)
    with func == 0b100110:
        #XOR
        alu_out |= (data0 ^ data1)
    with func == 0b000000:
        #SLL
        alu_out |= pyrtl.shift_left_logical(data1, sh)
    with func == 0b000010:
        #SRL
        alu_out |= pyrtl.shift_right_logical(data1, sh)
    with func == 0b000011:
        #SRA
        alu_out |= pyrtl.shift_right_arithmetic(data1, sh)
    with func == 0b101010:
        #SLT
        alu_out |= (data0 < data1)

rf[rd] <<= alu_out

