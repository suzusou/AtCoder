import math
N,X = map(int,input().split())
temp = math.ceil(X / N) 
print(chr(64 + temp))