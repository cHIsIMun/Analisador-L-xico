import argparse
from lexer import lex
from output_handler import write_output

def main():
    parser = argparse.ArgumentParser(description='Analisador lexico CLI')
    parser.add_argument('file', type=str, help='Arquivo para analisar')
    args = parser.parse_args()

    try:
        with open(args.file, 'r') as file:
            code = file.read()
            tokens, symbols, errors = lex(code)
            write_output(tokens, symbols)
            if errors:
                print("Erros encontrados:")
                for error in errors:
                    print(error)
            else:
                print("Nenhum erro lexico encontrado.")
    except FileNotFoundError:
        print(f"Error: The file {args.file} does not exist.")

if __name__ == '__main__':
    main()
