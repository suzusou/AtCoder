A,B,C = map(int,input().split())
temp = 1000
temp = min(temp,A)
temp = min(temp,B)
temp = min(temp,C)
print((A+B+C)-temp)