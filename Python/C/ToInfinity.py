S = input()
K = int(input())

if len(S) > K:
    print(S[K-1])
    exit()

for s in S:
    if s != "1":
        print(s)
        exit()

print("1")
