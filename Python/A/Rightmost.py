S = input()
index = -1

for s in range(len(S)):
    if S[s] == "a":
        index = s + 1

print(index)
        