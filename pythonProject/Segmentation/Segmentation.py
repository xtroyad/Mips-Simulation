import time

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
        circuit.print_data()
        cond = True
        instruction = ""
        instruction_to_mem = ""
        instruction_to_wb = ""
        pc_to_mem = -4
        pc_to_wb = -4
        ncicle = 1

        input("\nPress ENTER to continue\n")
        while(cond):
            print("#############################################################################################")
            print(f"CICLO {ncicle}")
            print("#############################################################################################")
            print()
            # WB
            self.writeB.execute(circuit.memwb, circuit, instruction_to_wb, pc_to_wb)
            # MEM
            circuit.memwb, instruction_to_wb, pc_to_wb = self.memAccess.execute(circuit.exmem, circuit, instruction_to_mem, pc_to_mem)
            # EX
            aux = self.exec.execute(circuit.idex, circuit, instruction)
            (circuit.exmem, instruction_to_mem, pc_to_mem) = aux
            # ID
            (circuit.idex, instruction) = self.decode.execute(circuit.ifid, circuit)
            # IF
            circuit.ifid = self.fetch.execute(circuit.pc, circuit)

            actualpc = circuit.pc.getDir()

            ncicle = 1 +ncicle
            # time.sleep(0.5)
            cond = (circuit.memwb != None or circuit.exmem != None or circuit.idex != None or  circuit.ifid != None)


