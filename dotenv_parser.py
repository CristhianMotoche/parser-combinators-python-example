import parsy as p

class EnvVar:
    def __init__(self, key, value):
        self.key = key
        self.value = value


key = p.regex(r"\w+")
equal = p.string("=")
value = p.regex(r"\w+")

key_val = p.seq((key << equal), value).combine(EnvVar)

dotenv_parser = key_val
