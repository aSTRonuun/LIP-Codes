def B():
  global string  
  print("Chamando B")
  if string[0] == '(':
    # Usando a regra  B - > ( RB   
    string = string[1:] # avanca caractere
    R()
    B()
  elif string[0] == '$':
    # B -> epsilon
    string = string[1:] # avanca caractere
  else:
    print("Erro sintático nao terminal B\n")    
  print("Saindo B")

def R():
  global string
  print("Chamando R")    
  if string[0] == ')':
    # Usando a regra  R - > (   
    string = string[1:] # avanca caractere
  elif string[0] == '(':
    # R -> ( RR
    string = string[1:] # avanca caractere
    R()
    R()  
  else:
    print("Erro sintático nao terminal R\n")  
  print("Saindo R")


string = "(())))$"
B()