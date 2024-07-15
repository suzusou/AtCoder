N = int(input())
A = list(map(int,input().split()))
Q = int(input())

L = [None] * Q
R = [None] * Q

for q in range(Q):
    L[q],R[q] = map(int,input().split())

hit = [0] * (N + 1)
miss = [0] * (N + 1)

for n in range(1,N + 1):
    if A[n - 1] == 1:
        hit[n] += hit[n - 1] + 1
        miss[n] += miss[n - 1]
    else:
        miss[n] += miss[n - 1] + 1
        hit[n] += hit[n - 1]

# print(hit)
# print(miss)

for q in range(Q):
    if hit[R[q]] - hit[L[q] - 1]  == miss[R[q]] - miss[L[q] - 1]:
        print("draw")
    elif hit[R[q]] - hit[L[q] - 1] > miss[R[q]] - miss[L[q] - 1]:
        print("win")
    else:
        print("lose")
# win 3 lose 1