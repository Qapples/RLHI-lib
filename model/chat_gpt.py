import openai
from model import ModelInterface as Interface

class ModelInterface(Interface):

    def __init__(self, model, temp):
        self.model = model
        self.temp = temp

    def generate_action_response(self, system_message: str, scenario: str) -> str:
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": scenario}
        ]
        
        response = openai.ChatCompletion.create(model=self.model, temperature=self.temp, messages=messages)
        text = response['choices'][0]['message']['content']

        return text