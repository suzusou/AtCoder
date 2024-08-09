n = int(input())
card = [tuple(map(int, input().split())) for _ in range(n)]

# 辞書型で元の順番を記憶しておく
d = {c_i: i for i, c_i in enumerate(card, 1)}

print("card",card)
print("d",d)

card.sort(reverse=True)
print("card",card)

cost = float("inf")
ans = []

for a, c in card:
    if cost >= c:
        cost = c
        ans.append(d[(a, c)])

print(ans)
print(len(ans))
print(*sorted(ans))

