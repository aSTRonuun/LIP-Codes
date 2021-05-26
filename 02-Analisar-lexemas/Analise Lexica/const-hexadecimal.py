import re

io = "0x23 0xFF 0x2F 0xG5 0xFF 0XA0000024"

regexp = r'0[x-X][a-fA-F]|[0-9]'

for re in re.finditer(regexp, io):
    print(re.re.fullmatch(regexp, io) != None)