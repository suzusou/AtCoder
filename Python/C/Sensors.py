import sys

sys.setrecursionlimit(1000000)

def SearchSharp(i,j):
    global H, W, mathSensor
    mathSensor[i][j] = "."
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if 0 <= di + i < H and 0 <= dj + j < W and  mathSensor[di + i][dj + j] == "#":
                SearchSharp(di + i, dj + j)


H, W = map(int, input().split())
mathSensor = []
SensorCount = 0

for h in range(H):
    mathSensor.append(list(input()))