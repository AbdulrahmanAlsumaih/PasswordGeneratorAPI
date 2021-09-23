from password_gen.config_json import ConfigJson
from password_gen.allowed_characters import AllowedCharacters


class Violations:

    def __init__(self, config: str, password: str):

        self.password = password
        self.config = config

    def characters(self) -> bool:

        config = ConfigJson(self.config)

        characters = AllowedCharacters(
            config.allowed_characters(), config.required_characters())
        characters.allowed_characters

        for i in self.password:
            if i not in characters.allowed_characters():
                return False

        for i in characters.assign_allowed_characters():
            a = sum(c in i["characters"] for c in self.password)
            if a >= i["occurrence"]:
                continue
            else:
                return False
        return True

    def length(self) -> bool:

        length = ConfigJson(self.config)

        if length.length() == None:
            if len(self.password) >= 8:
                return True
        elif len(self.password) >= length.length():
            return True
        else:
            return False

    def consecutive(self) -> bool:

        consecutive = ConfigJson(self.config)

        if consecutive.violations().get("consecutive") == None:
            return True

        occur, count, k = None, 0, consecutive.violations().get("consecutive")

        for i in self.password:
            if i == occur:
                count += 1
            else:
                occur, count = i, 1
            if count == k:
                return False

        return True

    def occurrence(self) -> bool:

        occurrence = ConfigJson(self.config)
        if occurrence.violations().get("occurrence") == None:
            return True

        occur, count, k = None, 0, occurrence.violations().get("occurrence")

        password = sorted(self.password)

        for i in password:
            if i == occur:
                count += 1
            else:
                occur, count = i, 1
            if count == k:
                return False
        return True

    def sequential(self) -> bool:

        sequential = ConfigJson(self.config)
        if sequential.violations().get("sequential") == None:
            return True
        else:
            allow_sequential = AllowedCharacters(
                sequential.allowed_characters(), sequential.violations().get("sequential"))

        num, upper, lower = 1, 1, 1
        list = {
            "numbers": num,
            'uppercase': upper,
            'lowercase': lower, }

        for i in range(len(self.password) - 1):
            for j in allow_sequential.assign_allowed_characters():

                if j["characters"].isdigit():

                    if self.password[i].isdigit() and self.password[i + 1].isdigit() and (
                        (ord(self.password[i]) - ord(self.password[i + 1]) == -1) or (
                            ord(self.password[i]) - ord(self.password[i + 1]) == 1)):

                        num += 1
                        list["numbers"] = num

                        if list["numbers"] == j["occurrence"]:
                            return False

                elif j["characters"].isupper():

                    if self.password[i].isupper() and self.password[i + 1].isupper() and (
                        (ord(self.password[i]) - ord(self.password[i + 1]) == -1) or (
                            ord(self.password[i]) - ord(self.password[i + 1]) == 1)):

                        upper += 1
                        list["uppercase"] = upper

                        if list["uppercase"] == j["occurrence"]:
                            return False

                elif j["characters"].islower():

                    if self.password[i].islower() and self.password[i + 1].islower() and (
                        (ord(self.password[i]) - ord(self.password[i + 1]) == -1) or (
                            ord(self.password[i]) - ord(self.password[i + 1]) == 1)):

                        list["lower"] = lower
                        lower += 1

                        if list["lowercase"] == j["occurrence"]:
                            return False
                else:
                    return True
        return True

    def verboten(self) -> bool:

        verboten = ConfigJson(self.config)

        if verboten.violations().get("verboten") == None:
            return True
        else:
            for key in verboten.violations().get("verboten"):
                if key in self.password:
                    return False
        return True
