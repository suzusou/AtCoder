S = input()
mojidict = {}

for s in S:
    if s in mojidict:
        mojidict[s] += 1
    else:
        mojidict[s] = 1

# mojidictのkeyでソート
mojidict_keys = sorted(mojidict)
mojidict = {k: mojidict[k] for k in mojidict_keys}

for moji,num in mojidict.items():
    if num == max(mojidict.values()):
        print(moji)
        exit()