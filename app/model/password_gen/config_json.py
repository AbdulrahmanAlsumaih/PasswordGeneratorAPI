import json


class ConfigJson:

    def __init__(self, config: str):
        self.config = json.loads(config)

    def length(self):

        return self.config.get("length")

    def allowed_characters(self):

        return self.config.get("allowed_characters")

    def required_characters(self):

        return self.config.get("required_characters")

    def violations(self):

        return self.config.get("violations")
