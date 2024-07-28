N = int(input())

while True:
    if int(str(N)[-3]) * int(str(N)[-2]) == int(str(N)[-1]):
        print(N)
        exit()
    N += 1