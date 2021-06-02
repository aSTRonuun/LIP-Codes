def dfa(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        remainder = string[1:]
        if (current, letter) in edges:
            newstate = edges[(current, letter)]
            return dfa(remainder, newstate, edges, accepting)
        return False


initial = 0
edges = {}

edges[(0,'+')] = 1

edges[(0,'-')] = 1

edges[(0,'')] = 1

digits = '0123456789'
for d in digits:
    edges[(1, d)] = 2

for d in digits:
    edges[(1, d)] = 1

edges[(1,'.')] = 2

for d in digits:
    edges[(2, d)] = 2

accepting = [2]

string = input()
print( dfa(string, initial, edges, accepting) )