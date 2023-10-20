from Circuit.Circuit import Circuit
from ControlUnit import ControlUnit
from HazardDetectionUnit import HazardDetectionUnit
from compiler import Compiler

if __name__ == '__main__':
    circuit = Circuit()
    compiler = Compiler()

    compiler.compile(circuit)

    uc = ControlUnit(circuit)
    uc.executeSegementation()

    print("fin")

    lol = input()
