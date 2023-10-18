
class Ex:
    def __init__(self):
        pass

    def execute(self, idex, circuit, instruction):




        if idex!=None:
            ###############################################################
            # Futuro registro exmem
            wb = idex[0]
            m = idex[1]

            aluResult = None
            rdata2 = None
            rDest = None
            ###############################################################

            [regDest, aluOp, aluSrc] = idex[2]


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
                aluResult = circuit.alu.ope(instruction, op1, op2)
            elif aluOp == 0b00: # Suma para dir en Mem
                aluResult = circuit.alu.ope("add", op1, op2)

            regD = idex[9] if regDest == 1 else idex[8]

            return [wb, m, aluResult, idex[6], regD]
        else:
            return None


