from Circuit.Alu import Alu, MainAlu, AddAlu
from Circuit.Mux import Mux

from Circuit.Pc import Pc

from Circuit.Memory import DataMem, IntructionMem, Registers
from Circuit.Signal import Signal
from HazardDetectionUnit import HazardDetectionUnit


class Circuit:

    def __init__(self):
        self.hd = HazardDetectionUnit(self)

        self.muxPc = Mux()
        self.signal = Signal()
        self.pc = Pc()
        self.dataMem = DataMem()
        self.instMem = IntructionMem()

        self.alu = MainAlu()
        self.aluPc = AddAlu()
        self.aluJump = AddAlu()

        self.registers = Registers()

        self.ifid = None
        self.idex = None
        self.exmem = None
        self.memwb = None

    def print_data(self):
        print("########################################")
        print("INSTRUCTIONS:")
        self.instMem.print_memory()
        print("########################################")
        print("DATAS:")
        self.dataMem.print_memory()
        print("########################################")

        print("REGISTERS:")
        self.registers.print_memory()

