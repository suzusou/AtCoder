N = int(input())
S = input()

boolean = False

for n in range(N):
    if S[n] == "x":
        print("No")
        exit()
    if S[n] == "o":
        boolean = True

if boolean:
    print("Yes")
else:
    print("No")