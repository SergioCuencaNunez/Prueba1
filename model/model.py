from abc import abstractmethod

class Model:
    def __init__(self, conf):
        self._conf = conf
    
    @abstractmethod
    def apply_model(self, problems):
        raise NotImplementedError()