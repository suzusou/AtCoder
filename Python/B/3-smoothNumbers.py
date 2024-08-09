N = int(input())

for x in range(100):
    for y in range(100):
        if (2**x) * (3**y) == N:
            print("Yes")
            exit()

print("No")