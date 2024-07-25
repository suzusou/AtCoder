N = str(bin(int(input())))
ans = 0

for n in range(len(N)-1,0,-1):
    if N[n] == "0":
        ans += 1
    else:
        break

print(ans)
