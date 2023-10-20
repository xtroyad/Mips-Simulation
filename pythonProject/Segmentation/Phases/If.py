class If:

    def __init__(self):
        pass

    def execute(self, pc, circuit):
        # El pc inicia en -4 pero si detectamos None es fin de programa
        if pc.getDir() == None:
            return None

        circuit.muxPc.setValue0(circuit.aluPc.ope("add", 4, pc.getDir()))

        concurrent_pc = circuit.muxPc.getValue()
        circuit.muxPc.setSignal(False)

        pc.updateConten(concurrent_pc)

        instruction = circuit.instMem.getData(concurrent_pc)


        new_pc = circuit.aluPc.ope("add", 4, concurrent_pc)

        return [new_pc, instruction]