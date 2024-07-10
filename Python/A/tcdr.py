S = input()
exclude = ["a","e","i","o","u"]
ans = ""

for s in S:
    if not s in exclude:
        ans += s

print(ans)

