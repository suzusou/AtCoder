S1 = input()
S2 = input()
S3 = input()
S4 = input()
Comparison = ["H","2B","3B","HR"]
ComparisonTemp = ["H","2B","3B","HR"]

for com in ComparisonTemp:
    if S1 == com:
        Comparison.remove(S1)
    elif S2 == com:
        Comparison.remove(S2)
    elif S3 == com:
        Comparison.remove(S3)
    elif S4 == com:
        Comparison.remove(S4)

if Comparison == []:
    print("Yes")
else:
    print("No")

