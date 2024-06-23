S = input()
small = 0
big = 0

for s in S:
    if s.islower():
        small += 1
    else:
        big += 1

if small > big:
    print(S.lower())
else:
    print(S.upper())