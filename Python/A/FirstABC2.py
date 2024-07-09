N = int(input())
S = input()

for s in range(len(S)-2):
    if S[s] == "A" and S[s+1] == "B" and S[s+2] == "C":
        print(s+1)
        exit()

print(-1)
