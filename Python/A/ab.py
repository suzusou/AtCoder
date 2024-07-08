N = int(input())
S = input()

for n in range(N-1):
    if (S[n] == 'a' and S[n+1] == 'b') or (S[n] == 'b' and S[n+1] == 'a'):
        print("Yes")
        exit()

print("No")
