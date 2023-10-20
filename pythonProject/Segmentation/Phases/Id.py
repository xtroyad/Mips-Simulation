class Id:
    def __init__(self):
        pass

    def callSystem(self, circuit): # Todo: podemos leer por teclado

        rdata1, rdata2 = circuit.hd.raw_detection("$v0", "$v0")
        if rdata1 == 10:
            circuit.ifid = None
            circuit.pc.updateConten(None)
            return (None, "")


    def execute(self, ifid, circuit):



        if ifid != None:  # Todo: Como veo que acaba
            ###############################################################
            # Futuro registro idex
            wb = []
            m = []
            ex = []
            new_pc = ifid[0]

            do_branch = (False,"")
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
            elif (instruction[0] == "beq" or instruction[0] == "bgt" or instruction[0] == "bne" or instruction[0] == "addi" ):

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

            return [wb, m, ex, new_pc, do_branch, rdata1, rdata2, im, rt, rd], instruction[0]

        else:
            return (None, "")
    def calculate_branch(self, d1, d2, op):
        if op == "beq":
            return True if d1 == d2 else False, "b"
        elif op == "bne":
            return True if d1 != d2 else False, "b"
        elif op == "bgt":
            return True if d1 > d2 else False, "b"
        elif op =="j":
            return (True, "j")
        else:
            return (False, "")