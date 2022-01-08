import collections

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
    
        n = len(board)
        trans = [0 for _ in range(n * n + 1)]
        i, j, k , d = n - 1, 0, 0, 1
        #(i,j)当前坐标，k格子编号，d横向移动方向
        while k < n * n :
            k += 1
            if board[i][j] == -1 :  #普通方格
                trans[k] = k
            else:       #带传送的方格
                trans[k] = board[i][j]
            if (d == 1 and j == n - 1) or (d == -1 and j == 0): #已到头
                d = -1 * d
                i -= 1
                continue    #提前结束本次，保证换行时列不变
            j += d

        step = 0
        vis = [False for _ in range(n*n + 1)]
        q = collections.deque()
        sq = collections.deque()  #步数队列，存储对应的步数
        q.append(1) #起点入队
        sq.append(0) #起点步数为0
        vis[1] = True
        found = False  #是否有解的标志

        while q:

            step_now = sq.popleft()
            get = q.popleft()
            if get == n * n :  #抵达终点
                found = True
                break


            for i in range(get + 1, min(get+6, n*n)+1):
                nextstep = trans[i]
                if not vis[nextstep]:
                    vis[nextstep] = True
                    q.append(nextstep)
                    sq.append(step_now + 1)
        
        return step_now if found else -1


board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
print(Solution().snakesAndLadders(board))
