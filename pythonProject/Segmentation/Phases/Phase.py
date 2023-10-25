from abc import ABC, abstractmethod

class Phase(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def view_phase(self, info):
        pass