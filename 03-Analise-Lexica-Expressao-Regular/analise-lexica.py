import re
import sys

class Token():
  def __init__(self,type, value, line, column):
    self.type = type
    self.value = value
    self.line = line
    self.column = column
  def __str__(self):
    return "Token(type='%s', value='%s', line=%d, column=%d)" % (self.type, self.value,self.line, self.column)

def tokenize(code):
    # palavras-chaves da linguagem analisada
    keywords = {'main', 'int', 'for', 'if', 'return', 'else', 'else if'}
    # lista com o identificador do token e a expressão regular que descreve o token    
    token_specification = [
        # Observe que a especificação do token NUMBER aceita números inteiros e decimais
        # Os números decimais descritos a parte inteira é obrigatória 
        ('NUMBER',   r'\d+(\.\d*)?'),   # Integer or decimal number
        ('ASSIGN',   r'='),             # Assignment operator
        ('END',      r';'),             # Statement terminator
        ('ID',       r'[A-Za-z]+'),     # Identifiers
        ('OP',       r'[+\-*/]'),       # Arithmetic operators
        ('NEWLINE',  r'\n'),            # Line endings
        ('SKIP',     r'[ \t]+'),        # Skip over spaces and tabs
        ('MISMATCH', r'.'),             # Any other character
        ('AP',       r'\('),            # Parêntese Abrindo
        ('OP',       r'\)'),            # Parêntese Fechando
        ('AC',       r'\{'),            # Colchetes Abrindo
        ('FC',       r'\}'),            # Colchetes Fechando
        ('OP',       r'\+|-|\/|\*'),    # Sinais de Operação
    ]
    
    # Com esse comando construímos uma expressão regular com todos os tokens da linguagem
    # Por exemplo,
    # tok_regex = (?P<NUMBER>\d+(\.\d*)|(?P<ID>[A-Za-z]+))
    # É uma expressão regular que descreve os tokens NUMBER e ID


    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    # A função finditer(tok_regex, code) devolve um iterador de match objects
    # Os atributos e métodos de match object mo utilizados são: 
    # * mo.lastgroup devolve o nome do último match capturado
    # * mo.group() devolve o último match encontrado
    # * mo.start() devolve o indice do inicio da substring casada pelo group
    

    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'ID' and value in keywords:
            kind = value
        elif kind == 'NEWLINE':
            # Cada vez que o caractere \n é encontrado o numero de linhas é incrementado            
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        yield Token(kind, value, line_num, column)

data = sys.stdin.readlines()

code = ''.join(data)


for token in tokenize(code):
    print(token)