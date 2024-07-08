S = input()
temp = 0

for s in range(len(S)-1,-1,-1):
    if S[s] == ".":
        temp = s
        break
print(S[temp+1:len(S)])