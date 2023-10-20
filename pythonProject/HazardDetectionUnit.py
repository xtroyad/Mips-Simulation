class HazardDetectionUnit:
    def __init__(self, circuit):
        self.circuit = circuit

        self.value1 = 0
        self.value2 = 0

    def raw_detection(self, r1, r2):
        self.value1 = self.circuit.registers.getData(r1)
        self.value2 = self.circuit.registers.getData(r2)

        idex = self.circuit.idex
        exmem = self.circuit.exmem
        memwb = self.circuit.memwb

        # Para accesos a memoria
        if idex!= None:
            # Esque tenemos un lw encima nuestro
            if idex[1][0] == 0b1 and self.raw_problem(r1, r2, exmem, 4):
                self.circuit.pc.updateConten(self.circuit.pc.getDir()-4)
                return None, None

        if memwb != None:
            # Ya le hemos puesto una burbuja en lw
            if memwb[0][1] == 0b1 and self.raw_problem(r1, r2, memwb, 3):
                self.raw(r1, r2, memwb, 3, 1)  # De memoria
                return self.value1, self.value2


        # Para operaciones normales
        if memwb != None :
            self.raw(r1, r2, memwb, 3, 2) # De calculo alu

        if exmem != None:
            self.raw(r1, r2, exmem, 4, 2)

        return self.value1, self.value2


    def raw_problem(self, r1, r2, reg, posrd):
        rd = reg[posrd]
        return r1 == rd or r2 == rd

    def raw(self, r1, r2, reg, posrd, post_data):
        rd = reg[posrd]

        if r1 == rd:
            self.value1 = reg[post_data]
        if r2 == rd:
            self.value2 = reg[post_data]






    #
    # def execution_raw(self, r1, r2):
    #     found = False
    #     rd = self.circuit.exmem[4]
    #     # Consultamos EXMEN para comprobar rd
    #     if r1 == rd:
    #         found = True
    #         self.value1 = self.circuit.exmem[2]
    #     if r2 == rd:
    #         found = True
    #         self.value2 = self.circuit.exmem[2]
    #     return found
    #
    # def memory_raw(self, r1, r2):
    #     found = False
    #     rd = self.circuit.memwb[3]
    #     # Consultamos EXMEN para comprobar rd
    #     if r1 == rd:
    #         found = True
    #         self.value1 = self.circuit.memwb[2]
    #     if r2 == rd:
    #         found = True
    #         self.value2 = self.circuit.memwb[2]
    #     return found