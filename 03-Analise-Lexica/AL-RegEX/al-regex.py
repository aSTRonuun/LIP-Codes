from typing import NamedTuple
import sys
import re

Token = NamedTuple('Token', [('type', str), ('value', str), ('line', int), ('column', int)])

def tokenize(code):
    keywords = {'for', 'if', 'return', 'else', 'else if'}
    
    token_specification = [
        ('NUMBER',   r'\d+(\.\d*)?'),   # Integer or decimal number
        ('ASSIGN',   r'='),             # Assignment operator
        ('END',      r';'),             # Statement terminator
        ('ID',       r'[A-Za-z]+'),     # Identifiers
        ('OP',       r'[+\-*/]'),       # Arithmetic operators
        ('NEWLINE',  r'\n'),            # Line endings
        ('SKIP',     r'[ \t]+'),        # Skip over spaces and tabs
        ('AP',       r'\('),            # Parêntese Abrindo
        ('FP',       r'\)'),            # Parêntese Fechando
        ('AC',       r'\{'),            # Colchetes Abrindo
        ('FC',       r'\}'),            # Colchetes Fechando
        ('COMMA',    r','),             # Vígula
        ('LEFTBRACKET', r'\['),         # Suporte Esquerdo
        ('RIGHTBRACKET', r'\]'),        # Suporte Direito
        ('LT',       r'\<'),            # Menor que

    ]
    

    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0

    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start

        if kind == 'ID' and value in keywords:
            kind = value
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        yield Token(kind, value, line_num, column)

#data = data = sys.stdin.readlines()

data = """
int main(){
  int a, b, c;
  int v[10];
  s = 0;  
  for(int i = 0; i < n; i = i + 1){
    s = s + i
  }  

  
  if (quantity) { 
    total = total + price * quantity + 34 + 1.23; 
  }
  return 0;
}

"""

code = ''.join(data)

for token in tokenize(code):
    print(token)