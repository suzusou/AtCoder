import sys
sys.setrecursionlimit(10 ** 9)

def f():
    if len(columns) != 1 and columns[-1] == columns[-2]:
        columns[-2] += 1
        del columns[-1]
        f()

N = int(input())
A = list(map(int,input().split()))

columns = []

for n in range(N):
    columns.append(A[n])
    f()

print(len(columns))