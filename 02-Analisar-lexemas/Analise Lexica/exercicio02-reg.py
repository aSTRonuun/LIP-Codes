import re

io = "2.34 5.3 .5 2."

pattern = r'\d+\.\d+'

print(re.findall(pattern, io))