from typing import List
'''博弈问题，通过状态递推，假定状态(i,j,k)，表示鼠在i，猫在j，当前已行动k步的情况
对于每一个行动者，比如鼠i，遍历当前可行动的位置graph[i]，如果其中有可使它必胜的点，则当前点亦必胜（走到下一个必胜点即可）；若没有，则搜索必平点；再没有，则必败
猫也同理。确定退出搜索的边界即可。'''

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:

        def dfs(i,j,k):  #i=鼠的位置，j=猫的位置，k=已行动步数（鼠先猫后）；结果0平局，1鼠胜，2猫胜
            #print(i,j,k)
            if k >= 2 * n :
                return 0
            if i == j :
                return 2    #猫鼠同位，猫胜
            if i == 0 :
                return 1    #老鼠进洞，鼠胜
            if k % 2 == 0 :   #已行动偶数步，鼠行动
                for i_nex in graph[i] :   #枚举鼠的下一步可行动位置
                    if vis[i_nex][j][k + 1] != -1 :
                        t = vis[i_nex][j][k + 1]
                    else :
                        t = dfs(i_nex, j, k + 1)
                        vis[i_nex][j][k + 1] = t
                    if t == 1 :
                        return 1    #若任意下一位置可使鼠胜，则鼠移动过去即必胜
                for i_nex in graph[i] :  #若未发现必胜位置，则再次遍历，尝试寻找平局位
                    if vis[i_nex][j][k + 1] != -1 :
                        t = vis[i_nex][j][k + 1]
                    else :
                        t = dfs(i_nex, j, k + 1)
                        vis[i_nex][j][k + 1] = t
                    if t == 0 :
                        return 0
                return 2   #若找不到必胜或必平，则必败
            else :    #奇数步，猫行动，注意猫不能进洞（0）
                for j_nex in graph[j] :
                    if j_nex == 0 :
                        continue
                    if vis[i][j_nex][k+1] != -1 :
                        t = vis[i][j_nex][k+1]
                    else :
                        t = dfs(i, j_nex, k + 1)
                        vis[i][j_nex][k+1] = t
                    if t == 2 :
                        return 2
                for j_nex in graph[j] :
                    if j_nex == 0 :
                        continue
                    if vis[i][j_nex][k+1] != -1 :
                        t = vis[i][j_nex][k+1]
                    else :
                        t = dfs(i, j_nex, k + 1)
                        vis[i][j_nex][k+1] = t
                    if t == 0 :
                        return 0
                return 1
        
        n = len(graph)
        vis = [[[-1 for _ in range(2 * n + 2)] for _ in range(n)]for _ in range(n)]        
        return dfs(1,2,0)

graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
graph = [[1,3],[0],[3],[0,2]]
print(Solution().catMouseGame(graph))