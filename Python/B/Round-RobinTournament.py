N = int(input())
S = [None] * N
temp = [None] * N

for n in range(N):
    S[n] = input()
    temp[n] = [S[n].count("o"),n + 1]


sort_data = sorted(temp, key=lambda x: (-x[0], x[1]))

for data in sort_data:
    print(data[1],end=" ")


