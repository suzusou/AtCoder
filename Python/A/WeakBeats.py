S = input()

for s in range(len(S)-1):
    if s % 2 == 0:
        if S[s+1] != "0":
            print("No")
            exit()

print("Yes")