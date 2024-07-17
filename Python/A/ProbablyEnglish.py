N = int(input())
W = list(input().split())
Search = ["and","not","that","the","you"]

for w in W:
    if w in Search:
        print("Yes")
        exit()
print("No")
