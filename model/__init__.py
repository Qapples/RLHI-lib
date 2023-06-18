import abc

class ModelResponseInterface():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def generate_resposne(self, system: str, scenario: str) -> str:
        return