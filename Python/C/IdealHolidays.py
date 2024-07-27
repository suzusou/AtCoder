N,A,B = map(int,input().split())
D = list(map(int,input().split()))
daymod = []
week = A + B

for d in D:
    daymod.append(d % week)
    daymod.append(d % week + week)

daymod.sort()

for i in range(N):
    l = daymod[i]
    r = daymod[i + N - 1]
    if r - l + 1 <= A:
        print("Yes")
        exit()

print("No")
