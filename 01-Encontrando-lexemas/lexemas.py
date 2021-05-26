def counting_lexemes(code, lexeme):
    n = 0
    n = code.count(lexeme)
    return n  
    

code = 'int main() { int a1, a2; a1 = a1 +a2 ; a2 = 2 * a1 ; return 0; }'
lexeme = 'a1'

print(counting_lexemes(code, lexeme))
 