N = int(input())
AB = []

for n in range(N):
    AB.append(list(map(int,input().split())))

for n in range(N):
    print(AB[n][0] + AB[n][1])
