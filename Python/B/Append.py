Q = int(input())
A = []

for q in range(Q):
    eg,value = map(int,input().split())
    if eg == 1:
        A.append(value)
    else:
        print(A[-value])