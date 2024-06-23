def max_sum_A(N, B):
    A = [0] * N
    A[0] = B[0]
    
    for i in range(1, N-1):
        A[i] = min(B[i-1], B[i])
    
    A[N-1] = B[N-2]
    
    #print("A:", A)
    #print("B:", B)

    return sum(A)



N = int(input())
B = list(map(int,input().split()))

print(max_sum_A(N, B))  