from yml_parser import parser


def test_yml_parser_parses_simple_scalar():
    text = "n:C"

    actual = parser.parse(text)
    expected = {'n': 'C'}

    assert actual == expected

def test_yml_parser_parses_scalar_long_name():
    text = "name:Cristhian"

    actual = parser.parse(text)
    expected = {'name': 'Cristhian'}

    assert actual == expected
