
class Wb:
    def __init__(self):
        pass
    def execute(self, memwb, circuit):
        if memwb != None:
            [regWrite, memToReg] = memwb[0]
            data = ""
            if memToReg:
                data = memwb[1]
            else:
                data = memwb[2]

            if regWrite == 0b1:
                circuit.registers.content[memwb[3]] = data