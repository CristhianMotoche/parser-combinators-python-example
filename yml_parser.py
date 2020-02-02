import parsec as p


colon = p.string(':')


@p.generate
def str_value():
    value = yield p.many(p.letter())
    return ''.join(value)


@p.generate
def scalar():
    name = yield str_value
    yield colon
    val = yield str_value
    return {name: val}

parser = scalar
