from Segmentation.Phases.Phase import Phase
from colorama import init, Fore, Back, Style
init(autoreset=True)

class Mem(Phase):
    def __init__(self):
        super().__init__()
    def execute(self, exmem, circuit, intruction, pcaux):
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
                memData = int(circuit.dataMem.content[aluResult])
            exit = [wb, memData, aluResult, regDest], intruction, pcaux
            self.view_phase([intruction, exmem, exit[0], pcaux])
            return exit
        else:
            self.printb("#############################################")
            self.printb(f"MEM (NULL)")
            self.printb("#############################################")
            print()
            print()
            return None, None, None

    def view_phase(self, info):
        intruction = info[0]
        exmem = info[1]
        memwb = info[2]
        pc = info[3]

        self.printb("#############################################")
        self.printb(f"MEM ({pc}) {intruction}")
        self.printb("#############################################")
        print()
        self.printb("EX/MEM register:")
        self.printb(f"|  |")
        self.printb(f"|  | WB =====> {exmem[0]} ")
        self.printb(f"|  |")
        self.printb(f"|  | M ======> {exmem[1]} ")
        self.printb(f"|  |")
        self.printb(f"|  | ALU R ==> {exmem[2]} ")
        self.printb(f"|  |")
        self.printb(f"|  | DATA 2 => {exmem[3]}")
        self.printb(f"|  |")
        self.printb(f"|  | REGD ===> {exmem[4]} ")
        self.printb(f"|  |")

        print()
        self.printb("MEM/WB register:")
        self.printb(f"           |  |")
        self.printb(f"WB =======>|  | {memwb[0]}")
        self.printb(f"           |  |")
        self.printb(f"MEM DATA =>|  | {memwb[1]} ")
        self.printb(f"           |  |")
        self.printb(f"ALU R ====>|  | {memwb[2]} ")
        self.printb(f"           |  |")
        self.printb(f"REGD =====>|  | {memwb[3]}")
        self.printb(f"           |  |")

    def printb(self, text):
        print(Fore.BLUE + text)