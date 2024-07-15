S = input()
portionString = set()

for ss in range(len(S)):
    for se in range(ss,len(S)):
        portionString.add(S[ss:se + 1])

print(len(portionString))

