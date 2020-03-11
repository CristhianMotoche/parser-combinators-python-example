import parsy as p

python_parser = p.string("Python").desc("The Awesome Python")
haskell_parser = p.string("Haskell")
java_parser = p.string("Java")
css_parser = p.string("CSS")

lang_parser = (
    python_parser
    | haskell_parser
    | java_parser
    | css_parser
    ).map(lambda lang: lang.lower())
