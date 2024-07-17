S = input()
ans = ""

for s in S:
    if s == "0":
        ans += "1"
    else:
        ans += "0"

print(ans)