# Aのindexを記録
# indexをリストにして辞書型でもっておく
# 5
# 2 2 3 3 5
# 33 40 2 12 16
# dict(2:[0,1],3[2,3],5:[4])

# for文外で最小の値を求める
# W[0],W[1]どちらが小さいか比較 同様にW[2],W[3]を比較

N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

index_dict = {}
for i in range(len(A)):
    if A[i] not in index_dict:
        index_dict[A[i]] = [i]
    else:
        index_dict[A[i]].append(i)

ans = 0

for key in index_dict:
    indices = index_dict[key]
    temp = []
    for tmp in indices:
        temp.append(W[tmp])
    temp.sort()
    ans += sum(temp[0:len(temp)-1])


print(ans)


