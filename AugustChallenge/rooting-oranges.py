class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        nRooted, nFresh = self.numberRootedFresh(grid)
        
        if nFresh == 0:
            return 0
        elif nRooted == 0:
            return -1
        else:
            anyRooted = True
            minutes = 0
            while anyRooted:
                
                grid, anyRooted = self.elapseMinute(grid)
                minutes += 1

            nRooted, nFresh = self.numberRootedFresh(grid)
            if nFresh == 0:
                return minutes - 1
            else:
                return -1
        
        
    def numberRootedFresh(self,grid):
        nRooted, nFresh = 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    nRooted += 1
                elif grid[i][j] == 1:
                    nFresh += 1
        return nRooted, nFresh
    
    
    def elapseMinute(self,grid):
        
        anyRooted=False
        newGrid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    newGrid[i][j] = 2
                if grid[i][j] == 1:
                    if self.isNeighbourRooted(i,j,grid):
                        newGrid[i][j] = 2
                        anyRooted = True
                    else:
                        newGrid[i][j] = 1
                        
        return newGrid, anyRooted
    
    
    def isNeighbourRooted(self,i,j,grid):
        if i > 0:
            if grid[i-1][j] == 2:
                return True
        if j+1 < len(grid[0]):
            if grid[i][j+1] == 2:
                return True
        if i+1 < len(grid):
            if grid[i+1][j] == 2:
                return True
        if j > 0:
            if grid[i][j-1] == 2:
                return True
        
        return False