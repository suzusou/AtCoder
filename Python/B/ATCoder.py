S = input()
ans = 0
temp = 0
acgt = ["A","C","G","T"]
for s in S:
    if s in acgt:
        temp += 1
        ans = max(ans,temp)
    else:
        temp = 0
print(ans)