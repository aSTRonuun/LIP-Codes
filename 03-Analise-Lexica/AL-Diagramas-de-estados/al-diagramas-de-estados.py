import sys

class Token():
  def __init__(self,type, value, line):
    self.type = type
    self.value = value
    self.line = line
    
  def __str__(self):
    return "Token(type='%s', value='%s', line=%d)" % (self.type, self.value,self.line) 

pos     = 0
token_atual = ""
proximoCaracter = ' '
line_num = 0

def pegaCaracter():
  global pos  
  global proximoCaracter
  if pos == len(code):
    proximoCaracter = '$'  
  else:
    proximoCaracter = code[pos] 
  pos = pos + 1

  
def acrescentaCaracter():
  global token_atual  
  token_atual = token_atual + proximoCaracter
     

def get_token():  
  global token_atual  
  global pos  
  global line_num
     
  keywords = {'main', 'if', 'else if', 'else', 'for', 'int'}

  pegaCaracter()
  while proximoCaracter == ' ' or proximoCaracter == '\n' or proximoCaracter == '\t' :
    if proximoCaracter == '\n':
        line_num = line_num + 1
    pegaCaracter()

  if proximoCaracter == '+':
    acrescentaCaracter()
    kind = 'OP'
    value = token_atual
  elif proximoCaracter == '*':
    acrescentaCaracter()
    kind = 'OP'
    value = token_atual
  elif proximoCaracter == ';':
    acrescentaCaracter()
    kind = 'END'
    value = token_atual
  elif proximoCaracter == '(':
      acrescentaCaracter()
      kind = '('
      value = token_atual
  elif proximoCaracter == ')':
      acrescentaCaracter()
      kind = ')'
      value = token_atual
  elif proximoCaracter == '{':
      acrescentaCaracter()
      kind = '{'
      value = token_atual
  elif proximoCaracter == '}':
      acrescentaCaracter()
      kind = '}'
      value = token_atual
  elif proximoCaracter == '$':
    kind = 'EOF'
    value = token_atual
  elif proximoCaracter.isalpha() :
    acrescentaCaracter()
    pegaCaracter()
    while proximoCaracter.isalpha() or proximoCaracter.isdigit() :
      acrescentaCaracter()
      pegaCaracter()
    pos = pos - 1    
    if token_atual in keywords:
      kind = token_atual
      value = token_atual  
    else:
      kind = 'ID'
      value = token_atual  
  elif proximoCaracter == ':':
      acrescentaCaracter()
      pegaCaracter()                
      if proximoCaracter == '=':      
        acrescentaCaracter()      
      kind = 'ASSIGN'
      value = token_atual
  else:
    kind = 'MISMATCH'
    value = ''             
  token_atual = ""  
  return Token(kind, value, line_num)  


#data = sys.stdin.readlines()
data = """
if(quantity){ 
    total = total + price * quantity + 34; 
}
"""

code = ''.join(data)

print(code)

token = get_token()
while  token.type != 'EOF':
  print(token)
  token = get_token()