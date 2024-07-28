N = int(input())
A = list(map(int,input().split()))

A = [a for a in A if a != max(A)]
print(max(A))