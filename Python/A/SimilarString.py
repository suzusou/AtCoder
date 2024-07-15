N = int(input())
S = input()
T = input()

for n in range(N):
    if not ((S[n] == "l" and T[n] == "1") or (S[n] == "1" and T[n] == "l") or (S[n] == "o" and T[n] == "0") or (S[n] == "0" and T[n] == "o") or S[n] == T[n]):
        print("No")
        exit()

print("Yes")