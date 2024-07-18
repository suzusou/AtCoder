Y,M,D = map(int,input().split('/'))
daymax = [0,31,28,31,30,31,30,31,31,30,31,30,31]

# 閏年の判定
if Y % 400 == 0 or (Y % 4 == 0 and Y % 100 != 0):
    daymax[2] = 29

while not(Y % (M * D) == 0):
    if M == 12 and D == 31:
        Y += 1
        M = 1
        D = 1
    elif D == daymax[M]:
        M += 1
        D = 1
    elif D < daymax[M]:
        D += 1


str_type = str("{:0>4}".format(Y))+"/"+str("{:0>2}".format(M))+"/"+str("{:0>2}".format(D))
print(str_type)

