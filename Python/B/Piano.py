moji = "wbwbwwbwbwbw"
S = ""

for i in range(150):
    S += moji

W,B = map(int,input().split())
length = W + B

for ss in range(len(S)):
    for se in range(0,len(S),length):
        if S[ss:se + 1].count("w") == W and S[ss:se + 1].count("b") == B:
            print("Yes")
            exit()

print("No")

