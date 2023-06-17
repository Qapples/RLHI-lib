import abc
import random

def _get_rand_int(len):
    return random.randint(0, len - 1)

class BaseScenarioProvider:
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def get_categories(self) -> tuple[str]:
        return
    
    @abc.abstractmethod
    def get_domains(self) -> tuple[str]:
        return
    
    @abc.abstractmethod
    def get_entropies(self) -> tuple[str]:
        return
    
    @abc.abstractmethod
    def get_regions(self) -> tuple[str]:
        return
    
    @abc.abstractmethod
    def get_scopes(self) -> tuple[str]:
        return
    
    @abc.abstractmethod
    def get_severities(self) -> tuple[str]:
        return
    
    @abc.abstractmethod
    def get_systems(self) -> tuple[str]:
        return
    
    def get_category(self, index) -> str:
        return self.get_categories()[index]
    
    def get_domain(self, index) -> str:
        return self.get_domains()[index]
    
    def get_entropy(self, index) -> str:
        return self.get_entropies()[index]

    def get_region(self, index) -> str:
        return self.get_regions()[index]
    
    def get_scope(self, index) -> str:
        return self.get_scopes()[index]
    
    def get_severity(self, index) -> str:
        return self.get_severities()[index]
    
    def get_system(self, index) -> str:
        return self.get_systems()[index]
    
    
    def get_random_category(self) -> str:
        return self.get_category(_get_rand_int(len(self.get_categories())))
    
    def get_random_domain(self) -> str:
        return self.get_domain(_get_rand_int(len(self.get_domains())))
    
    def get_random_entropy(self) -> str:
        return self.get_entropy(_get_rand_int(len(self.get_entropies())))
    
    def get_random_region(self) -> str:
        return self.get_region(_get_rand_int(len(self.get_regions())))
    
    def get_random_scope(self) -> str:
        return self.get_scope(_get_rand_int(len(self.get_scopes())))
    
    def get_random_severity(self) -> str:
        return self.get_severity(_get_rand_int(len(self.get_severities())))
    
    def get_random_system(self) -> str:
        return self.get_system(_get_rand_int(len(self.get_systems())))
