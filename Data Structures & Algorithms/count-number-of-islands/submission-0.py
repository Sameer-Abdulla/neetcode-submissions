class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r<0 or r==row or c<0 or c==col or grid[r][c]=='0' or (r, c) in visit):
                return 1
            visit.add((r, c))
            print(visit)
            return ( 1 *
                dfs(r, c+1) *
                dfs(r, c-1) *
                dfs(r+1, c) *
                dfs(r-1, c)
            )
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i,j) not in visit :
                    print(f"r:{res}, p:({i, j})")
                    res += dfs(i, j) 

        return res  
grid=[["1","1","0","0","1"],
      ["1","1","0","0","1"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]]



        