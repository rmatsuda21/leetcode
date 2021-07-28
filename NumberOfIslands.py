# https://leetcode.com/problems/number-of-islands/

from collections import deque

"""
:type grid: List[List[str]]
:rtype: int
"""
def numIslands(grid):
    queue = deque()
    islands = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if (grid[y][x] == '1'):
                islands += 1
                queue.append((x, y))
            
            while queue:
                i, j = queue.pop()
                grid[j][i] = '2'
                
                if j > 0 and grid[j-1][i] == '1':
                    queue.append((i, j-1))
                if j < len(grid)-1 and grid[j+1][i] == '1':
                    queue.append((i, j+1))
                if i > 0 and grid[j][i-1] == '1':
                    queue.append((i-1, j))
                if i < len(grid[j])-1 and grid[j][i+1] == '1':
                    queue.append((i+1, j))
                
    return islands

# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numIslands(grid))