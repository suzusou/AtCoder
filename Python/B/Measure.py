N = int(input())

j_lst = [j for j in range(1, 10) if N % j == 0]
s = ['-'] * (N + 1)

for i in range(N + 1):
    for x in j_lst:
        if i % (N // x) == 0:
            s[i] = str(x)
            break
ans = ''.join(s)
print(ans)


