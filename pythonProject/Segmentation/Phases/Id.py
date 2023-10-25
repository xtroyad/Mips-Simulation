from Segmentation.Phases.Phase import Phase
from colorama import init, Fore, Back, Style
init(autoreset=True)


class Id(Phase):
    def __init__(self):
        super().__init__()

    def callSystem(self, circuit):

        rdata1, rdata2 = circuit.hd.raw_detection("$v0", "$v0")
        if rdata1 == 10:
            circuit.ifid = None
            circuit.pc.updateConten(None)
            return (None, "")

    def execute(self, ifid, circuit):

        if ifid != None:
            self.printr("#############################################")
            self.printr(f"ID ({ifid[0] - 4}) {ifid[1]}")
            self.printr("#############################################")
            print()
            ###############################################################
            # Futuro registro idex
            wb = []
            m = []
            ex = []
            new_pc = ifid[0]

            do_branch = (False, "")
            rdata1 = 0
            rdata2 = 0
            im = 0
            rt = ""
            rd = ""
            ###############################################################
            instruction = ifid[1]

            # Tenemos una llamada a sistema
            if instruction[0] == "syscall":
                return self.callSystem(circuit)

            # Las señales de control
            wb, m, ex = circuit.signal.updateSignals(instruction[0])

            # Instrucciones aritmeticologicas
            if instruction[0] == "add" or instruction[0] == "sub":

                rd = instruction[1]

                r1 = instruction[2]
                r2 = instruction[3]

                rdata1, rdata2 = circuit.hd.raw_detection(r1, r2)
            # Carga de memoria
            elif (instruction[0] == "lw"):
                rs = instruction[2]
                rt = instruction[1]

                rdata1, rdata1 = circuit.hd.raw_detection(rs, rs)

                im = int(instruction[3])


            # Carga en memoria
            elif (instruction[0] == "sw"):
                rs = instruction[2]
                rt = instruction[1]

                rdata1, rdata2 = circuit.hd.raw_detection(rs, rt)

                im = int(instruction[3])

            elif instruction[0] == "j":
                im = int(instruction[1])
                do_branch = self.calculate_branch(rdata1, rdata2, instruction[0])


            # Tipo I
            elif (instruction[0] == "beq" or instruction[0] == "bgt" or instruction[0] == "bne" or instruction[0] == "addi"):

                r1 = instruction[1]
                r2 = instruction[2]
                if instruction[0] == "addi":
                    rdata1, rdata1 = circuit.hd.raw_detection(r2, r2)
                else:
                    rdata1, rdata2 = circuit.hd.raw_detection(r1, r2)

                do_branch = self.calculate_branch(rdata1, rdata2, instruction[0])

                im = int(instruction[3])
                if instruction[0] == "addi":
                    rt = instruction[1]

            # En las comprobaciones de raw hemos tenido que meter una burbuja
            if rdata1 == None and rdata2 == None:
                return None, ""

            exit = [wb, m, ex, new_pc, do_branch, rdata1, rdata2, im, rt, rd], instruction
            self.view_phase([[new_pc, instruction], exit[0]])

            return exit

        else:
            self.printr("#############################################")
            self.printr(f"ID (NULL)")
            self.printr("#############################################")
            print()
            print()
            return (None, "")

    def view_phase(self, info):
        ifid = info[0]
        idex = info[1]



        self.printr("IF/ID register:")
        self.printr(f"|  |")
        self.printr(f"|  | PC+4 ===> {ifid[0]}")
        self.printr(f"|  |")
        self.printr(f"|  | INTRUC => {ifid[1]} ")
        self.printr(f"|  |")
        print()
        self.printr("ID/EX register:")
        self.printr(f"         |  |")
        self.printr(f"WB =====>|  | {idex[0]}")
        self.printr(f"         |  |")
        self.printr(f"M ======>|  | {idex[1]} ")
        self.printr(f"         |  |")
        self.printr(f"EX =====>|  | {idex[2]}")
        self.printr(f"         |  |")
        self.printr(f"NEW PC =>|  | {idex[3]} ")
        self.printr(f"         |  |")
        self.printr(f"BRANCH =>|  | {idex[4]}")
        self.printr(f"         |  |")
        self.printr(f"DATA 1 =>|  | {idex[5]} ")
        self.printr(f"         |  |")
        self.printr(f"DATA 2 =>|  | {idex[6]}")
        self.printr(f"         |  |")
        self.printr(f"IM === =>|  | {idex[7]} ")
        self.printr(f"         |  |")
        self.printr(f"REGD 1 =>|  | {idex[8]} ")
        self.printr(f"         |  |")
        self.printr(f"REGD 2 =>|  | {idex[9]} ")
        self.printr(f"         |  |")



    def printr(self, text):
        print(Fore.RED  + text)

    def calculate_branch(self, d1, d2, op):
        if op == "beq":
            return True if d1 == d2 else False, "b"
        elif op == "bne":
            return True if d1 != d2 else False, "b"
        elif op == "bgt":
            return True if d1 > d2 else False, "b"
        elif op == "j":
            return (True, "j")
        else:
            return (False, "")
