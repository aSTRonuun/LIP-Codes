import re


regexp = r'0[Xx]([a-fA-F]+|[0-9]+|[0-9a-fA-F]+|[a-fA-F0-9]+)'


for string in input().split(' '):
    print(re.fullmatch(regexp, string) != None)