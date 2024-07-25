S = input()
T = input()

dist1_set = {"AB", "AE", "BA", "BC", "CB", "CD", "DC", "DE", "EA", "ED"}
S_is_dist1 = S in dist1_set
T_is_dist1 = T in dist1_set

if S_is_dist1 == T_is_dist1:
    print("Yes")
else:
    print("No")
