from Circuit.Circuit import Circuit
from ControlUnit import ControlUnit
from Compiler import Compiler

if __name__ == '__main__':
    circuit = Circuit()
    compiler = Compiler()

    compiler.compile(circuit)

    uc = ControlUnit(circuit)
    uc.executeSegementation()

    print("EXIT")

    lol = input()
