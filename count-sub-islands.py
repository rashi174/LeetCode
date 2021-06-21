'''
1905. Count Sub Islands

You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

 

Example 1:


Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
Example 2:


Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2 
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.
 

Constraints:

m == grid1.length == grid2.length
n == grid1[i].length == grid2[i].length
1 <= m, n <= 500
grid1[i][j] and grid2[i][j] are either 0 or 1.
'''


class Solution:
    def __init__(self):
        self.all=[]
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        islands = self.numIslands(grid2)
        return self.comp(grid1,islands)

    def numIslands(self, grid):
        number_of_islands=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    lands=[]
                    self.dfs(grid,i,j,lands)
                    number_of_islands+=1
                    self.all.append(lands)
        return self.all

    def dfs(self,grid,i,j,lands):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!=1 :
            return 0
        lands.append((i,j))
        grid[i][j]=0 #visited
        #Look for island in every direction
        self.dfs(grid,i-1,j,lands)
        self.dfs(grid,i+1,j,lands)
        self.dfs(grid,i,j-1,lands)
        self.dfs(grid,i,j+1,lands)

    def comp(self,grid1,list1):
        c=0
        for i in list1:
            flag=True
            for x,y in i:
                if grid1[x][y] !=1:
                    flag=False
                    break
            if flag:
                c+=1
        return c
