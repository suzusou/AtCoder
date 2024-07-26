trump = list(map(int,input().split()))
trumpset = list(set(trump))

card1 = trump.count(trumpset[0])
card2 = trump.count(trumpset[1])

if (card1 == 3 and card2 == 2) or (card2 == 3 and card1 == 2):
    print("Yes")
else:
    print("No")

