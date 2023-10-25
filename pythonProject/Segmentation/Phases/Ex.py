from Segmentation.Phases.Phase import Phase
from colorama import init, Fore, Back, Style
init(autoreset=True)

class Ex(Phase):
    def __init__(self):
        super().__init__()

    def execute(self, idex, circuit, instruction):

        if idex!=None:
            self.printg("#############################################")
            self.printg(f"EX ({idex[3] - 4}) {instruction}")
            self.printg("#############################################")
            ###############################################################
            # Futuro registro exmem
            wb = idex[0]
            m = idex[1]

            aluResult = None
            rdata2 = None
            rDest = None
            ###############################################################

            [regDest, aluOp, aluSrc] = idex[2]

            do_branch, type_b = idex[4]

            if do_branch:
                jum_result = 0

                if type_b == "j":
                    jum_result = idex[7]
                else:
                    jum_result = circuit.aluJump.ope("add", idex[3], idex[7]*4)
                print("The jump will finally be made. The pipiline will be cleaned for failing the prediction")
                circuit.muxPc.setValue1(jum_result)
                circuit.muxPc.setSignal(True)
                circuit.ifid = None

            # Calculo de la ALU
            op1 = idex[5]
            op2 = 0

            if aluSrc == 0b1: # Viene del inmediato
                op2 = idex[7]
            else:             # Viene del banco de registros
                op2 = idex[6]

            aluResult = 0

            # Simulamos ALU control
            if aluOp == 0b10: #Tipo R
                aluResult = circuit.alu.ope(instruction[0], op1, op2)
            elif aluOp == 0b00: # Suma para dir en Mem
                aluResult = circuit.alu.ope("add", op1, op2)

            regD = idex[9] if regDest == 1 else idex[8]
            exit = [wb, m, aluResult, idex[6], regD]

            self.view_phase([instruction, idex, exit])

            return exit, instruction, idex[3]-4
        else:
            self.printg("#############################################")
            self.printg(f"EX (NULL)")
            self.printg("#############################################")
            print()
            print()
            return None, None, None


    def view_phase(self, info):
        intruction = info[0]
        idex = info[1]
        exmen = info[2]


        print()
        self.printg("ID/EX register:")
        self.printg(f"|  |")
        self.printg(f"|  | WB =====> {idex[0]}")
        self.printg(f"|  |")
        self.printg(f"|  | M ======> {idex[1]} ")
        self.printg(f"|  |")
        self.printg(f"|  | EX =====>{idex[2]}")
        self.printg(f"|  |")
        self.printg(f"|  | NEW PC => {idex[3]} ")
        self.printg(f"|  |")
        self.printg(f"|  | BRANCH => {idex[4]}")
        self.printg(f"|  |")
        self.printg(f"|  | DATA 1 => {idex[5]} ")
        self.printg(f"|  |")
        self.printg(f"|  | DATA 2 => {idex[6]}")
        self.printg(f"|  |")
        self.printg(f"|  | IM === => {idex[7]} ")
        self.printg(f"|  |")
        self.printg(f"|  | REGD 1 => {idex[8]} ")
        self.printg(f"|  |")
        self.printg(f"|  | REGD 2 => {idex[9]} ")
        self.printg(f"|  |")

        print()
        self.printg("EX/MEM register:")
        self.printg(f"         |  |")
        self.printg(f"WB =====>|  | {exmen[0]} ")
        self.printg(f"         |  |")
        self.printg(f"M ======>|  | {exmen[1]} ")
        self.printg(f"         |  |")
        self.printg(f"ALU R ==>|  | {exmen[2]} ")
        self.printg(f"         |  |")
        self.printg(f"DATA 2 =>|  | {exmen[3]}")
        self.printg(f"         |  |")
        self.printg(f"REGD ===>|  | {exmen[4]} ")
        self.printg(f"         |  |")

    def printg(self, text):
        print(Fore.GREEN + text)
