import re

io = """
int main(){
    int a2, b2, conta_prox;
    a = 56;
    b = 67;
}
"""

inteiro = r'[0-9]+'
identificador = r'[a-zA-Z][a-zA-Z0-9_]+'

print(re.findall(inteiro, io))
print(re.findall(identificador, io))