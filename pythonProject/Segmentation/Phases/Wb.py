from Segmentation.Phases.Phase import Phase
from colorama import init, Fore, Back, Style
init(autoreset=True)

class Wb(Phase):
    def __init__(self):
        super().__init__()
    def execute(self, memwb, circuit, instuction, pcaux):
        if memwb != None:
            [regWrite, memToReg] = memwb[0]
            data = ""
            if memToReg:
                data = memwb[1]
            else:
                data = memwb[2]

            if regWrite == 0b1:
                circuit.registers.content[memwb[3]] = data
            self.view_phase([instuction, memwb, pcaux])
            circuit.print_data()
        else:
            self.printb("#############################################")
            self.printb(f"WB (NULL)")
            self.printb("#############################################")
            print()
            print()
    def view_phase(self, info):
        intruction = info[0]
        memwb = info[1]
        pc = info[2]

        self.printb("#############################################")
        self.printb(f"WB ({pc}) {intruction}")
        self.printb("#############################################")

        print()
        self.printb("MEM/WB register:")
        self.printb(f"|  |")
        self.printb(f"|  | WB =======> {memwb[0]}")
        self.printb(f"|  |")
        self.printb(f"|  | MEM DATA => {memwb[1]} ")
        self.printb(f"|  |")
        self.printb(f"|  | ALU R ====> {memwb[2]} ")
        self.printb(f"|  |")
        self.printb(f"|  | REGD =====> {memwb[3]}")
        self.printb(f"|  |")

    def printb(self, text):
        print(Fore.MAGENTA  + text)