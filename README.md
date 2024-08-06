
# Analisador Léxico

## Descrição
Este documento fornece instruções sobre como utilizar o analisador léxico desenvolvido para uma linguagem de programação simplificada. O analisador foi implementado em Python e é capaz de identificar tokens, classificar identificadores e gerar uma tabela de símbolos, além de reportar erros léxicos.

## Estrutura do Projeto
O projeto está dividido nos seguintes arquivos:
- `tokens.py`: Define os tipos de tokens e suas expressões regulares.
- `lexer.py`: Contém a lógica do analisador léxico.
- `main.py`: Script principal que executa o analisador.
- `output_handler.py`: Manipula a saída, formatando e salvando os resultados.

## Configuração
Clone o repositório do projeto usando o seguinte comando:
```bash
git clone https://github.com/cHIsIMun/Analisador-Lexico.git
```
Navegue até o diretório do projeto:
```bash
cd Analisador-Lexico
```

## Execução
Para executar o analisador, use o seguinte comando no terminal:
```bash
python main.py arquivo.code
```
Substitua `arquivo.code` pelo caminho do arquivo de código-fonte que você deseja analisar.

## Saída
A saída do analisador será um arquivo `output.json` contendo:
- Uma lista de `tokens` identificados, cada um com os campos:
  - `token`: A palavra identificada no código.
  - `identificacao`: Descrição do token e seu tipo ou função.
  - `tamanho`: Número de caracteres do token.
  - `posicao`: Posição do token no código (linha, coluna).
- Uma `tabela de símbolos` que mapeia identificadores únicos a seus índices correspondentes.

## Erros
O analisador também identifica e reporta erros léxicos, listando caracteres ou sequências que não correspondem a nenhum token válido.

## Suporte
Para suporte técnico ou contribuições, por favor, abra uma issue no repositório do GitHub ou envie um pull request com suas sugestões ou correções.
