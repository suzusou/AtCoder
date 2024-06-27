A = []

while True:
    temp = int(input())
    A.append(temp)
    if temp == 0:
        break

A.reverse()

for a in A:
    print(a)

