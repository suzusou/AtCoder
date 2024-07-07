# 2分探索
import bisect
a = [2, 3, 5, 7, 11, 13, 17, 19]
print(bisect.bisect_left(a, 2)) # 左側の挿入点を返す　0
print(bisect.bisect_right(a, 2)) # 右側の挿入点を返す　1
print(bisect.bisect(a, 2)) # 右側の挿入点を返す　1


# book/A11.pyを参照
N,X = map(int,input().split())
A = list(map(int,input().split()))

# ans = bisect.bisect(A,X)
# print(ans)

L = 0
R = N 

while L <= R:
    M = (L + R) // 2
    if X < A[M]:
        R = M - 1
    elif X == A[M]:
        print(M)
        exit()
    else:
        L = M + 1