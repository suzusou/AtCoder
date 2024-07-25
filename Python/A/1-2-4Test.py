A,B = map(int,input().split())
ans = set()

for n in range(2,-1,-1):
    if A - (2**n) >= 0:
        ans.add(2**n)
        A -= 2**n 
    if B - (2**n) >= 0:
        ans.add(2**n)
        B -= 2**n


print(sum(ans))