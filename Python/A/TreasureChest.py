N = int(input())
S = input()

boolean = False

for s in S:
    if s == "|":
        boolean = not(boolean)
    if s == "*" and boolean:
        print("in")
        exit()

print("out")