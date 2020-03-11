from dotenv_parser import dotenv_parser

def test_parser_returns_key_value():
    input_ = "USER=cmotoche"
    output = dotenv_parser.parse(input_)

    assert output.key == "USER"
    assert output.value == "cmotoche"
