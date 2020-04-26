from collections import namedtuple

Result = namedtuple("Result", ("status", "text", "index"))

SUCCESS = 1
ERROR = 0

class Parser:

    def __init__(self, fn):
        self.fn = fn

    def __call__(self, text, index):
        return self.fn(text, index)

    def parse(self, text):
        result = self(text, 0)

        if result.status:
            return result
        else:
            raise ParseError(result)

    def __or__(self, other):
        return choice(self, other)

    def __rshift__(self, other):
        return skip_left(self, other)

    def __lshift__(self, other):
        return skip_right(self, other)


class ParseError(Exception):

    def __init__(self, result):
        self.result = result

    def __str__(self):
        return f"unexpected input: {self.result.text} at {self.result.index}"


def string(s):
    @Parser
    def string_parser(text, index):
        slen = len(s)
        if text[index:index + slen] == s:
            return Result(status=SUCCESS, index=index + slen, text=s)
        else:
            return Result(status=ERROR, index=index, text=text)
    return string_parser


def choice(parser, other):
    @Parser
    def choice_parser(text, index):
        res = parser(text, index)
        return res if res.status else other(text, index)
    return choice_parser


def skip_left(left_parser, parser):
    @Parser
    def skip_left_parser(text, index):
        res = left_parser(text, index)
        return res if not res.status else parser(text, res.index)
    return skip_left_parser



def skip_right(parser, right_parser):
    @Parser
    def skip_right_parser(text, index):
        res = parser(text, index)
        res_right = right_parser(text, res.index)
        return res if res_right.status else res_right
    return skip_right_parser


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

l_bracket = string("[")
r_bracket = string("]")

lang_closed_parser = l_bracket >> lang_parser << r_bracket
