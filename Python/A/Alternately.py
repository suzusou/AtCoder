N = int(input())
S = input()

if N == 1:
    print("Yes")
    exit()

for n in range(N - 1):
    if S[n] == S[n + 1]:
        print("No")
        exit()

print("Yes")


