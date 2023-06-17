import abc
from random import Random

class BaseScenarioProvider:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self._random = Random()

    def generate_scenario(self, category, domain, entropy, region, scope, severity) -> str:
        return f"Random word: {entropy}\nScope: {scope}\nSeverity: {severity}\nRegion: {region}\nCategory: {category}\nDomain: {domain}\n"
    
    def generate_random_scenario(self) -> str:
        category = self.get_random_category()
        domain = self.get_random_domain()
        entropy = self.get_random_entropy()
        region = self.get_random_region()
        scope = self.get_random_scope()
        severity = self.get_random_severity()

        return self.generate_scenario(category, domain, entropy, region, scope, severity)

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
        return self._random.choice(self.get_categories())
    
    def get_random_domain(self) -> str:
        return self._random.choice(self.get_domains())
    
    def get_random_entropy(self) -> str:
        return self._random.choice(self.get_entropies())
    
    def get_random_region(self) -> str:
        return self._random.choice(self.get_regions())
    
    def get_random_scope(self) -> str:
        return self._random.choice(self.get_scopes())
    
    def get_random_severity(self) -> str:
        return self._random.choice(self.get_severities())
    
    def get_random_system(self) -> str:
        return self._random.choice(self.get_systems())
