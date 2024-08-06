from tokens import token_regex
import sys

def lex(code):
    token_list = []
    symbol_table = {}
    symbol_index = 1
    line_num = 0
    line_start = 0
    errors = []

    for mo in token_regex.finditer(code):
        kind = mo.lastgroup
        value = mo.group(kind)
        column = mo.start() - line_start
        length = len(value)

        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            error_msg = f'Erro: Charactere inesperado {value!r} na posicao {line_num},{column}'
            errors.append(error_msg)
            continue 

        if kind in ['IDENTIFIER', 'NUMBER']:
            if value not in symbol_table:
                symbol_table[value] = symbol_index
                symbol_index += 1
            identificacao = f'{kind.lower()}, {symbol_table[value]}'
        else:
            identificacao = kind.lower()

        token_list.append({
            "token": value,
            "identificacao": identificacao,
            "tamanho": length,
            "posicao": [line_num, column]
        })

        if '\n' in value:
            line_num += value.count('\n')
            line_start = mo.end()

    return token_list, symbol_table, errors
