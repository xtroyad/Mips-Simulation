class HazardDetectionUnit:
    def __init__(self, circuit):
        self.circuit = circuit

        self.value1 = 0
        self.value2 = 0

    def raw_detection(self, r1, r2):
        self.value1 = self.circuit.registers.getData(r1)
        self.value2 = self.circuit.registers.getData(r2)

        exmem = self.circuit.exmem
        memwb = self.circuit.memwb

        self.raw(r1, r2, memwb, 3)
        self.raw(r1, r2, exmem, 4)



        return self.value1, self.value2

    def raw(self, r1, r2, reg, posrd):
        rd = reg[posrd]

        if r1 == rd:
            self.value1 = reg[2]
        if r2 == rd:
            self.value2 = reg[2]




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