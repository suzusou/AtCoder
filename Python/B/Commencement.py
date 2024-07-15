S = input()
mojidict = {}
temp = []

for s in S:
    if s in mojidict: 
        mojidict[s] += 1
    else:
        mojidict[s] = 1

for i in mojidict.values():
    temp.append(i)

for tmp in temp:
    if temp.count(tmp) != 2:
        print("No")
        exit()

print("Yes")


