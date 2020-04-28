from dotenv_parser import dotenv_parser

def test_parser_returns_key_value():
    input_ = "USER=cmotoche"
    output = dotenv_parser.parse(input_)

    assert output[0].key == "USER"
    assert output[0].value == "cmotoche"

def test_parser_returns_lifst_of_items():
    with open(".env") as f:
        input_ = f.read()
    output = dotenv_parser.parse(input_)

    assert len(output) == 3
