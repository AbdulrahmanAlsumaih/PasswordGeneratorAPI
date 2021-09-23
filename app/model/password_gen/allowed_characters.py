import string


class AllowedCharacters:

    def __init__(self, allowed: str, required: str):

        self.allowed = allowed
        self.required = required

    def exctract_allowed_characters(self):

        list = []
        for i in self.required:
            list.append(
                {
                    "occurrence": i[0],
                    "characters": self.allowed[i[1] + 's'][i[2]]
                })

        return list

    def assign_allowed_characters(self) -> str:

        list = []
        char = None
        for i in self.exctract_allowed_characters():

            if i["characters"] in 'ascii_letters':
                char = string.ascii_letters
            elif i["characters"] in 'ascii_lowercase':
                char = string.ascii_lowercase
            elif i["characters"] in 'ascii_uppercase':
                char = string.ascii_uppercase
            elif i["characters"] in 'digits':
                char = string.digits
            elif i["characters"] in 'hexdigits':
                char = string.hexdigits
            elif i["characters"] in 'octdigits':
                char = string.octdigits
            elif i["characters"] in 'punctuation':
                char = string.punctuation
            elif i["characters"] in 'printable':
                char = string.printable
            elif i["characters"] in 'whitespace':
                char = string.whitespace
            else:
                char = i["characters"]
            list.append(
                {
                    "occurrence": i['occurrence'],
                    "characters": char
                })
        return list

    def allowed_characters(self) -> str:
        all = ''
        for i in self.allowed.values():
            for j in list(i.values()):
                if j in 'ascii_letters':
                    all += string.ascii_letters
                elif j in 'ascii_lowercase':
                    all += string.ascii_lowercase
                elif j in 'ascii_uppercase':
                    all += string.ascii_uppercase
                elif j in 'digits':
                    all += string.digits
                elif j in 'hexdigits':
                    all += string.hexdigits
                elif j in 'octdigits':
                    all += string.octdigits
                elif j in 'punctuation':
                    all += string.punctuation
                elif j in 'printable':
                    all += string.printable
                elif j in 'whitespace':
                    all += string.whitespace
                else:
                    all += j
        return all
