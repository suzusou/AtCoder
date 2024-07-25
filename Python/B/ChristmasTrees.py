A,M,L,R = map(int,input().split())
right = (R - A) // M
left =  (A - L) // M
# print(right)
# print(left)
print(right + left + 1)