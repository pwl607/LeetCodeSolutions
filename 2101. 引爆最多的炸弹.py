'''AC'''

def Solution(bombs):
    
    n = len(bombs)

    '''炸弹i可以引爆炸弹j的条件：(xi-xj)**2 + (yi-yj)**2 <= xr**2'''
    '''建立一个有向图，若炸弹i可以引爆炸弹j，添加一条边：i -> j'''
    '''edges[i] = [j1, j2, ...]表明存在有向边i -> j1, i -> j2, ...'''
    edges = [[]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2 <= (bombs[i][2]) ** 2 :
                edges[i].append(j)
    print(edges)

    '''统计图的分块数，用vis[i]记录节点是否访问过，tot进行计数（这一块里有几个节点），并更新维护其最大值'''
    ans = 0

    def work(i):  #当前节点i
        nonlocal vis
        nonlocal tot
        if not vis[i]:
            vis[i] = True   #标记访问
            tot += 1
            for j in edges[i]:  #枚举i指向的j
                if not vis[j]:
                    work(j)        

    for i in range(n):  #枚举从i出发最多可以到达多少节点，即点炸弹i可以引爆多少个炸弹
        tot = 0
        vis = [False for _ in range(n)]
        work(i)
        ans = max(tot, ans)
        if ans == n :
            break   #如果已经可以引爆所有炸弹，不用继续尝试了

    return ans

'''Input'''
bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
#bombs = [[1,1,5],[10,10,5]]
bombs = [[2,1,3],[6,1,4]]

'''Output'''
print(Solution(bombs))