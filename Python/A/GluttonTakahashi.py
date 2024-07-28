N = int(input())
S = []

for _ in range(N):
    S.append(input())

for n in range(N - 2):
    if S[n] == "sweet" and S[n + 1] == "sweet":
        print("No")
        exit()

print("Yes")
