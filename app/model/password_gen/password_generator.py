from model.password_gen.violations import Violations
from model.password_gen.config_json import ConfigJson
from model.password_gen.allowed_characters import AllowedCharacters

import secrets


class PasswordGenerator:

    def __init__(self, config: str):

        self.config = config

    def new(self) -> str:

        config = ConfigJson(self.config)
        length = config.length()
        if length == None:
            length = 8

        allow = AllowedCharacters(
            config.allowed_characters(), config.required_characters())

        all = allow.allowed_characters()

        while True:
            password = ''.join(secrets.choice(all) for i in range(length))
            if (self.allowed(password)):
                break
        return password

    def allowed(self, password: str) -> bool:
        self.password = password

        check = Violations(self.config, self.password)

        if check.consecutive() and check.occurrence() and check.verboten() and check.length() and check.characters() and check.sequential():
            return True
        return False
