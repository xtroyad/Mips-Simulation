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

            do_branch = 0
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
                rdata1 = circuit.registers.getData(rs)

                rt = instruction[1]

                im = instruction[3]

            # Salto incondicional
            elif instruction[0] == "j":
                circuit.pc.updateConten(instruction[1])
            # Salto condicional
            elif (instruction[0] == "beq" or instruction[0] == "bne" or instruction[0] == "addi"):

                r1 = instruction[1]
                r2 = instruction[2]

                rdata1, rdata2 = circuit.hd.raw_detection(r1, r2)

                do_branch = self.calculate_branch(rdata1, rdata2, instruction[0])

                im = int(instruction[3])

                rt = instruction[1]

            return [wb, m, ex, new_pc, do_branch, rdata1, rdata2, im, rt, rd], instruction[0]

        else:
            return (None, "")
    def calculate_branch(self, d1, d2, op):
        if (op == "beq"):
            return d1 == d2
        if (op == "bne"):
            return d1 != d2
