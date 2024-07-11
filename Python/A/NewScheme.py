S = list(map(int,input().split()))
prev = S[0]

for s in S:
    if s % 25 != 0 or s < 100 or s > 675 or prev > s:
        print("No")
        exit()
    prev = s

print("Yes")