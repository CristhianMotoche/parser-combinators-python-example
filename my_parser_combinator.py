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

    def __or__(self, other):
        return choice(self, other)


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


def choice(parser, other):
    @Parser
    def choice_parser(text):
        res = parser(text)
        return res if res else other(text)
    return choice_parser


python_parser = string("Python")
haskell_parser = string("Haskell")
java_parser = string("Java")
js_parser = string("JavaScript")
css_parser = string("CSS")

lang_parser = (
      python_parser
    | haskell_parser
    | java_parser
    | js_parser
    | css_parser
)
