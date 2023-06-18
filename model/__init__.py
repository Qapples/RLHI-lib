import abc

class ModelInterface():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def generate_action_resposne(self, system: str, scenario: str) -> str:
        return