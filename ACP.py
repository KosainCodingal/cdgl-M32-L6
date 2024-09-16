def validPath(maze, i, j, m, n):
    if (i == m or j == n) or (maze[i][j] == 1): return False
    return True

def ratMaze(maze, i, j, m, n, arr):
    if arr[-1][-1] == 1: return True
    if validPath(maze, i, j, m, n):
        arr[i][j] = 1
        if ratMaze(maze, i+1, j, m, n): return True
        if ratMaze(maze, i, j+1, m, n): return True
        arr[i][j] = 0
    return False

maze = [
    [0,1,0,1,1],
    [0,0,0,0,0],
    [1,0,1,0,1],
    [0,0,1,0,0],
    [1,0,0,1,0]
]

arr = [0 for i in range(len(maze[0]))]
for j in range(len(maze)):
    ratMaze(maze, 0, 0, len(maze), len(maze[0]), arr)
    for i in arr: print(i)
    