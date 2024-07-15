N = int(input())
S = input()
if N % 2 == 0:
    Mid = N / 2
else:
    Mid = N // 2 + 1

ACount = 0
TCount = 0

for s in S:
    if s == "A":
        ACount += 1
    if s == "T":
        TCount += 1
    if Mid <= ACount or Mid <= TCount:
        print(s)
        exit()

# if ACount > TCount:
#     print("A")
# else:
#     print("T")