def gr(K, row, column):
    if K == 0:
        return

    for n in range(int(3**(K-1) + row), int(2*(3**(K-1)) + row)):
        for m in range(int(3**(K-1) + column), int(2*(3**(K-1)) + column)):
            ban[n][m] = "."

    K -= 1

    for n in range(3):
        for m in range(3):
            if n != 1 or m != 1:
                gr(K, row + n * (3**K), column + m * (3**K))

N = int(input())
ban = [["#" for _ in range(3**N)] for _ in range(3**N)]
if N == 0:
    print("#")
else:
    gr(N, 0, 0)
    for row in ban:
        print("".join(row))
