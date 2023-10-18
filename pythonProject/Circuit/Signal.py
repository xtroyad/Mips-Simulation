class Signal:

    def __init__(self):
        self.regDest = 0b0
        self.pcSrc = 0b0
        self.memRead = 0b0
        self.memToReg = 0b0
        self.aluOp = 0b00
        self.memWrite = 0b0
        self.aluSrc = 0b0
        self.regWrite = 0b0

    def updateSignals(self, op):
        if (op =="sub" or op =="add"):
            self.regDest = 0b1
            self.pcSrc = 0b0
            self.memRead = 0b0
            self.memToReg = 0b0
            self.aluOp = 0b10
            self.memWrite = 0b0
            self.aluSrc = 0b0
            self.regWrite = 0b1
        if (op =="addi"):
            self.regDest = 0b0
            self.pcSrc = 0b0
            self.memRead = 0b0
            self.memToReg = 0b0
            self.aluOp = 0b0
            self.memWrite = 0b0
            self.aluSrc = 0b1
            self.regWrite = 0b1


        if (op =="lw"):
            self.regDest = 0b0
            self.pcSrc = 0b0
            self.memRead = 0b1
            self.memToReg = 0b1
            self.aluOp = 0b00
            self.memWrite = 0b0
            self.aluSrc = 0b1
            self.regWrite = 0b1

        if (op == "sw"):
            # self.regDest = x
            self.pcSrc = 0b0
            self.memRead = 0b0
            # self.memToReg = x
            self.aluOp = 0b00
            self.memWrite = 0b1
            self.aluSrc = 0b1
            self.regWrite = 0b0

        if (op == "beq" or op =="bne" or op == "j"):
            # self.regDest = x
            self.pcSrc = 0b1
            self.memRead = 0b0
            # self.memToReg = x
            self.aluOp = 0b01
            self.memWrite = 0b0
            self.aluSrc = 0b0
            self.regWrite = 0b0

        return ([self.regWrite, self.memToReg], [self.memRead, self.memWrite], [self.regDest, self.aluOp, self.aluSrc])
