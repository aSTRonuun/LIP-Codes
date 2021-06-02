import re


regexp = r'(1*01*01*)*'


for string in input().split(' '):
    print(re.fullmatch(regexp, string) != None)