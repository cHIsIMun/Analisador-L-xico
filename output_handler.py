import json

def write_output(tokens, symbols):
    with open('saída.json', 'w') as f:
        json.dump({'tokens': tokens, 'symbols': symbols}, f, indent=2)
