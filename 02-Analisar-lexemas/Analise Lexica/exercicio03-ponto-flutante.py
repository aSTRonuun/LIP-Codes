import re

code = input()

pattern = r'(\d+\.)|(\.\d+)'

for s in code.split():
    if re.findall(pattern, s):
        print(s)