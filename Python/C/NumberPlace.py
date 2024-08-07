import copy

def rowCheck(gridrow):
    for g in gridrow:
        g.sort()
        if g != [1,2,3,4,5,6,7,8,9]:
            return False
    return True

def columnsCheck(gridcolumns):
    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(gridcolumns[j][i])
        temp.sort()
        if temp != [1,2,3,4,5,6,7,8,9]:
            return False
    return True

def ThreeAndThree(gridThree):
    for row in range(0,9,3):
        for columns in range(0,9,3):
            temp = []
            for i in range(3):
                for j in range(3):
                    temp.append(gridThree[i+row][j+columns])
            temp.sort()
            if temp != [1,2,3,4,5,6,7,8,9]:
                return False
    return True

grid = []

for _ in range(9):
    grid.append(list(map(int,input().split())))

gridrow = copy.deepcopy(grid)
gridcolumns = copy.deepcopy(grid)
gridThree = copy.deepcopy(grid)

if rowCheck(gridrow) and columnsCheck(gridcolumns) and ThreeAndThree(gridThree):
    print("Yes")
else:
    print("No")


