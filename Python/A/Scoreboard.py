N = int(input())
X = [None]*N
Y = [None]*N
for n in range(N):
    X[n],Y[n] = map(int,input().split())

if sum(X) == sum(Y):
    print("Draw")
elif sum(X) > sum(Y):
    print("Takahashi")
else:
    print("Aoki")

# print(X)
# print(Y)