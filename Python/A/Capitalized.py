S = input()

if 65 <= ord(S[0]) <= 90: 
    for s in range(1, len(S)):
        if not (97 <= ord(S[s]) <= 122):
            print("No")
            exit()
else:
    print("No")
    exit()
print("Yes")

# S = input()
# print("Yes" if S.istitle() else "No")

