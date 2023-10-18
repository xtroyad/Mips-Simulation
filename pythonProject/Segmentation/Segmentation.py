from Segmentation.Phases.If import If
from Segmentation.Phases.Id import Id
from Segmentation.Phases.Ex import Ex
from Segmentation.Phases.Mem import Mem
from Segmentation.Phases.Wb import Wb


class Segmentation:

    def __init__(self):

        self.fetch = If()
        self.decode = Id()
        self.exec = Ex()
        self. memAccess = Mem()
        self. writeB = Wb()

    def execute(self, circuit):
        cond = True
        instruction = ""

        while(cond):
            # WB
            self.writeB.execute(circuit.memwb, circuit)
            # MEM
            circuit.memwb = self.memAccess.execute(circuit.exmem, circuit)
            # EX
            aux = self.exec.execute(circuit.idex, circuit, instruction)
            circuit.exmem = aux
            # ID
            (circuit.idex, instruction) = self.decode.execute(circuit.ifid, circuit)
            # IF
            circuit.ifid = self.fetch.execute(circuit.pc, circuit)

            cond = (circuit.memwb != None or circuit.exmem != None or circuit.idex != None or  circuit.ifid != None)
