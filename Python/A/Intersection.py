L1,R1,L2,R2 = map(int,input().split())
print(min(R1,R2) - max(L1,L2) if min(R1,R2) - max(L1,L2) >= 0 else 0)