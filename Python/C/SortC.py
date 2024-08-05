N=int(input())
A=list(map(int,input().split()))
ans=[]

for i in range(N):
    A[i]-=1

for i in range(N):
    while A[i]!=i:
        ans.append((i+1,A[i]+1))
        pre=A[A[i]]
        A[A[i]]=A[i]
        A[i]=pre
        
print(len(ans))
for i in ans:
    print(*i)
