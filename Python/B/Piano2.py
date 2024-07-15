N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
coupling = sorted(A + B)
temp = 0

for c in range(0,len(coupling)-1):
    for a in A:
        if coupling[c] == a or coupling[c + 1] == a:
            temp += 1
    if temp == 2:
        print("Yes")
        exit()
    temp = 0


print("No")