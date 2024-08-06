import re

token_specs = [
    ('WHILE', r'\bwhile\b'),
    ('DO', r'\bdo\b'),
    ('IDENTIFIER', r'\b[ij]\b'),
    ('NUMBER', r'\b\d+\b'),
    ('OPERATOR', r'[<+=]'),
    ('TERMINATOR', r'[;]'),
    ('SKIP', r'[ \t\n]+'),
    ('MISMATCH', r'.'),
]

token_regex = re.compile('|'.join('(?P<%s>%s)' % pair for pair in token_specs))
