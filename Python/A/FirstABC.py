N = int(input())
S = input()
juge = []

for n in range(N):
    if not S[n] in juge:
        juge.append(S[n])
    if len(juge) == 3:
        print(n + 1)
        exit()