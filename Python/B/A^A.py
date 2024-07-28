B = int(input())

for n in range(1,19):
    if n ** n == B:
        print(n)
        exit()

print(-1)




