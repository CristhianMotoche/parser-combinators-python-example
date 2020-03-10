class Parser:

    def __init__(self, fn):
        self.fn = fn

    def __call__(self, text):
        return self.fn(text)

    def parse(self, text):
        result = self(text)

        if result:
            return result
        else:
            raise ParseError(text)


class ParseError(Exception):

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return "unexpected input: '%s'" % self.text


def string(s):
    @Parser
    def string_parser(text):
        if text == s:
            return s
        else:
            return None
    return string_parser
