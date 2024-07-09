N = input()
if len(N) == 1:
    print("Yes")
    exit()


for n in range(len(N)-1):
    if int(N[n]) <= int(N[n+1]):
            print("No")
            exit()

print("Yes")