import re

io = "a1 2b cc3 44d"

patter = r'[a-z][0-9]'

print(re.findall(patter,io))