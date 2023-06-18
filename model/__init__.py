import abc
import yaml
from . import DEFAULT_SYSTEM_ACTION_MESSAGE 

class ModelInterface():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def generate_action_resposne(self, scenario: str, system_message: str = DEFAULT_SYSTEM_ACTION_MESSAGE) -> str:
        return

    def save_action_response_yaml(self, yaml_file_path: str, scenario: str, scenario_file_path: str, action_response: str, action_file_path: str, system_message: str = DEFAULT_SYSTEM_ACTION_MESSAGE):
        metadata = {
            "original_scenario": scenario,
            "scenario_filepath": scenario_file_path,
            "action": action_response,
            "action_filepath": action_file_path,
            "system_message": system_message,
        }

        with open(yaml_file_path, 'w') as yaml_file:
            yaml.dump(metadata, yaml_file)

        with open(action_file_path, 'w') as action_file:
            action_file.write(action_response)