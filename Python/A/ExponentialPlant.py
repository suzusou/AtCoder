H = int(input())

for i in range(1,1000000):
    if 2**i-1 > H:
        print(i)
        exit()

# print(1<<3)

