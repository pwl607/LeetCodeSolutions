'''AC'''
'''
「以扣会友」线下活动所在场地由若干主题空间与走廊组成，场地的地图记作由一维字符串型数组 grid，字符串中仅包含 "0"～"5" 这 6 个字符。地图上每一个字符代表面积为 1 的区域，其中 "0" 表示走廊，其他字符表示主题空间。相同且连续（连续指上、下、左、右四个方向连接）的字符组成同一个主题空间。

假如整个 grid 区域的外侧均为走廊。请问，不与走廊直接相邻的主题空间的最大面积是多少？如果不存在这样的空间请返回 0。

例子
grid = ["11111100000",
        "21243101111",
        "21224101221",
        "11111101111"]
不与走廊相邻的区域有[2,2,2] [4] [3] [4] [2,2]共5个，其中最大面积是3，输出3
'''

from typing import List


class Solution:
    def largestArea(self, grid: List[str]) -> int:
        '''使用FloodFill计算面积，若与走廊相邻（碰到'0'或者出界）则令面积为0'''
        def fill(i,j,s):  #当前位置(i,j)，当前统计区域的字符为s
            nonlocal flag
            if i < 0 or i >= m or j < 0 or j >= n :  #出界，判定为与走廊相邻
                flag = True  #即使判定与走廊相邻，也需要完成遍历，以做好访问标记
                return
            if grid[i][j] == '0' :  #碰到真正的走廊
                flag = True
                return
            nonlocal vis
            if grid[i][j] == s and not vis[i][j]:
                nonlocal area
                area += 1
                vis[i][j] = True
                fill(i-1, j, s)
                fill(i, j-1, s)
                fill(i, j+1, s)
                fill(i+1, j, s)

        m = len(grid)
        n = len(grid[0])
        vis = [[False for _ in range(n)]for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] in ['1','2','3','4','5']:
                    area = 0
                    flag = False   #Flag=True表示碰到了走廊
                    fill(i,j,grid[i][j])
                    if flag :
                        area = 0
                    ans = max(area, ans)
        return ans

'''Input'''
grid = ["11111100000","21243101111","21224101221","11111101111"]
grid = ["554350243","325420343","333515002","054425245","041533100","345521331","114302205","555403522","101315123","111034215"]

'''Output'''
print(Solution().largestArea(grid))