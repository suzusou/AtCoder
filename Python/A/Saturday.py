S = input()
week = ["","Friday","Thursday", "Wednesday", "Tuesday","Monday"]

for w in range(len(week)):
    if S == week[w]:
        print(w)
        exit()

