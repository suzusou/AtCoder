import bisect

N,T = map(int,input().split())
S = input()
X = list(map(int,input().split()))

list0 = []
list1 = []
ant0 = []
ant1 = []
ans = 0

for s in range(len(S)):
    if S[s] == "1":
        list1.append(s)
    else:
        list0.append(s)

for li in list0:
    ant0.append(X[li])
ant0.sort()

for li in list1:
    ant1.append(X[li])
ant1.sort()

# print(ant0)
# print(ant1)

for i in range(len(ant0)):
    xxx=bisect.bisect_left(ant1,ant0[i]-(T*2))
    yyy=bisect.bisect_right(ant1,ant0[i]-1)
    # print(xxx)
    # print(yyy)
    ans+=yyy-xxx

print(ans)






