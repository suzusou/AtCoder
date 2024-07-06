S = input()
T = input()
mojidictS = {}
mojidictT = {}
tempCountS = 0
tempCountT = 0
tempCount = 0

for s in S:
    if s in mojidictS:
        mojidictS[s] += 1
    else:
        mojidictS[s] = 1

for t in T:
    if t in mojidictT:
        mojidictT[t] += 1
    else:
        mojidictT[t] = 1

if '@' in mojidictS:
    CoverCountS = mojidictS['@']
else:
    CoverCountS = 0

if '@' in mojidictT:
    CoverCountT = mojidictT['@']
else:
    CoverCountT = 0

for key in mojidictS.keys():
    if key not in mojidictT:
        if key != '@':
            if key not in ['a','t','c','o','d','e','r']:
                print("No")
                #print(key)
                exit()
            else:
                tempCountT += mojidictS[key]
                #print("skey"+key)
    else:
        if mojidictS[key] != mojidictT[key] and key != '@':
            if key not in ['a','t','c','o','d','e','r']:
                print("No")
                #print(key)
                exit()
            else:
                if mojidictS[key] < mojidictT[key]:
                    tempCountS += mojidictT[key] - mojidictS[key]


for key in mojidictT.keys():
    if key not in mojidictS:
        if key != '@':
            if key not in ['a','t','c','o','d','e','r']:
                print("No")
                #print(key)
                exit()
            else:
                tempCountS += mojidictT[key]
                #print("tkey"+key)
    else:
        if mojidictS[key] != mojidictT[key] and key != '@':
            if key not in ['a','t','c','o','d','e','r']:
                print("No")
                #print(key)
                exit()
            else:
                if mojidictT[key] < mojidictS[key]:
                    tempCountT += mojidictS[key] - mojidictT[key]



if CoverCountS-tempCountS >= 0 and CoverCountS-tempCountS >= 0:
    print("Yes")
else:
    print("No")

# print(mojidictS)
# print(mojidictT)

# print("CoverCountS:" + str(CoverCountS))
# print("CoverCountT:" + str(CoverCountT))
# print("tempCountS:" + str(tempCountS))
# print("tempCountT:" + str(tempCountT))
# print("tempCount:" + str(tempCount))
