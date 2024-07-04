N = int(input())
temp = ["L","n","g"]

for n in range(1,N+1):
    temp.insert(n,"o")

for t in temp:
    print(t,end="")