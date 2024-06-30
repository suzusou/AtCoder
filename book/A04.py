import math
N = int(input())
ans = ""
i = 8

while True:
    if math.floor(N / (2<<i)) == 1:
        ans += "1"
        N -= 2<<i
    else:
        ans += "0"

    if i == 0:
        if N == 1:
            ans += "1"
        else:
            ans += "0"
        break

    i -= 1

print(ans)

