class Parser:

    def __init__(self, fn):
        self.fn = fn

    def __call__(self, text):
        return self.fn(text)
