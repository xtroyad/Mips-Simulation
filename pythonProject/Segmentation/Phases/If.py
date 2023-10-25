from Segmentation.Phases.Phase import Phase
from colorama import init, Fore, Back, Style
init(autoreset=True)

class If(Phase):

    def __init__(self):
        super().__init__()

    def execute(self, pc, circuit):
        # El pc inicia en -4 pero si detectamos None es fin de programa
        if pc.getDir() == None:
            self.printy("#############################################")
            self.printy(f"IF (NULL)")
            self.printy("#############################################")
            return None

        circuit.muxPc.setValue0(circuit.aluPc.ope("add", 4, pc.getDir()))

        concurrent_pc = circuit.muxPc.getValue()
        circuit.muxPc.setSignal(False)

        pc.updateConten(concurrent_pc)

        instruction = circuit.instMem.getData(concurrent_pc)


        new_pc = circuit.aluPc.ope("add", 4, concurrent_pc)

        exit = [concurrent_pc, instruction]
        self.view_phase(exit)
        return [new_pc, instruction]

    def view_phase(self, info):
        self.printy("#############################################")
        self.printy(f"IF ({info[0]}) {info[1]}")
        self.printy("#############################################")

        print()
        self.printy("IF/ID register:")

        self.printy(f"         |  |")
        self.printy(f"PC+4 ===>|  | {info[0]+4}")
        self.printy(f"         |  |")
        self.printy(f"INTRUC =>|  | {info[1]} ")
        self.printy(f"         |  |")
        print()


    def printy(self, text):
        print(Fore.YELLOW + text)

