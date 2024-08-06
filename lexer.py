from tokens import token_regex
import sys

def lex(code):
    token_list = []
    symbol_table = {}
    symbol_index = 1
    line_num = 0
    line_start = 0
    errors = []
    next_token_is_function = False

    for mo in token_regex.finditer(code):
        kind = mo.lastgroup
        value = mo.group(kind)
        column = mo.start() - line_start
        length = len(value)

        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            errors.append(f'Erro: Charactere inesperado {value!r} na posicao {line_num},{column}')
            continue
        
        if kind == 'IDENTIFIER':
            if value not in symbol_table:
                symbol_table[value] = {"index": symbol_index, "type": "variable", "line_declared": line_num}
                symbol_index += 1
            if next_token_is_function:
                symbol_table[value]["type"] = "function"
            identificacao = f'identifier, {symbol_table[value]["index"]} ({symbol_table[value]["type"]})'
        else:
            identificacao = kind.lower()

        token_list.append({
            "token": value,
            "identificacao": identificacao,
            "tamanho": length,
            "posicao": [line_num, column]
        })

        next_token_is_function = (value == '(') 

        if '\n' in value:
            line_num += value.count('\n')
            line_start = mo.end()

    return token_list, symbol_table, errors
