'''2021-12-30 AC'''

def Solution(isConnected):
    n = len(isConnected)
    vis = [False for _ in range(n)]  #是否到访过标记
    res = 0  #结果

    def work(i): #访问城市i
        vis[i] = True

        for j in range(n) :  #枚举可能与i相连的城市j
            if isConnected[i][j] == 1 and i != j and not vis[j]:
                work(j)
    
    for i in range(n):
        if not vis[i]:
            work(i)
            res += 1
    return res



'''Input'''
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
isConnected = [[1,0,0],[0,1,0],[0,0,1]]

'''Output'''
print(Solution(isConnected))