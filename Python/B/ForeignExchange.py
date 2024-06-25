N = int(input()) #N番目の通貨が最大になるものを求める
A = list(map(int,input().split())) #国それぞれの通貨の価格
S = []
for i in range(N-1):
    S.append(list(map(int,input().split())))

for a in range(len(A)-1):
    A[a+1] += A[a]//S[a][0]*S[a][1]

print(A[len(A)-1])

# N=4
# A=5 7 0 3
# 2 2 国1から国2への通貨の価格
# 4 3 国2から国3への通貨の価格
# 5 2 国3から国4への通貨の価格

