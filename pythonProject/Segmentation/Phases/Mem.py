
class Mem:
    def __init__(self):
        pass
    def execute(self, exmem, circuit):
        if exmem != None:

            wb = exmem[0]
            [memRead, memWrite] = exmem[1]

            aluResult = exmem[2]
            reg2Data = exmem[3]
            regDest = exmem[4]

            memData = 0
            if memWrite == 0b1:
                circuit.dataMem.content[aluResult] = reg2Data
            if memRead == 0b1:
                memData = circuit.dataMem.content[aluResult]

            return [wb, memData, aluResult, regDest]
        else:
            return None


