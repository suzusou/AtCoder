S = input()

if S[0] == "<" and S[len(S)-1] == ">":
    for s in range(1,len(S)-1):
        if S[s] != "=":
            print("No")
            exit()
    print("Yes")

else:
    print("No")
