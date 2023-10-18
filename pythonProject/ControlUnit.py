from Segmentation.Segmentation import Segmentation


class ControlUnit:
    def __init__(self, circuit):
        self.circuit = circuit
        self.segmentation = Segmentation()

    def executeSegementation(self):
        self.segmentation.execute(self.circuit)


