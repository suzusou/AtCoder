A,B = map(int,input().split())
print("Yes" if B-A == 1 and A % 3 != 0 else "No")