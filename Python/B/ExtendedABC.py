S = input()
a = S.count('A')
b = S.count('B')
c = S.count('C')

if 'A' * a + 'B' * b + 'C' * c == S:
    print('Yes')
    exit()
    
print('No')