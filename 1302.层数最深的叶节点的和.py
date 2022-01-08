'''2012-12-30 Accepted'''

from typing import List

class TreeNode:
    '''定义树的节点类型'''
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def makeTree(l:List) -> TreeNode :
    '''由输入列表生成树，返回其根节点'''
    q = []
    if not l :
        return
    root = TreeNode(val=l.pop(0))
    q.append(root)
    while q :
        t = q.pop(0)
        if l:
            if l[0] != 'null':
                t.left = TreeNode(val=l.pop(0))
                q.append(t.left)
            else:
                l.pop(0)
        if l:
            if l[0] != 'null':
                t.right = TreeNode(val=l.pop(0))
                q.append(t.right)
            else:
                l.pop(0)
    return root



'''Solve'''
def Solution(root:TreeNode) -> int :
    import collections
    sum_of_level = [0]  #记录第i层的和
    q = collections.deque()  #BFS队列
    qd = collections.deque()  #队列中节点的对应深度
    if not root :
        return 0  #输入空树返回0
    q.append(root)  #树根入队
    qd.append(0)
    while q :
        cur_root = q.popleft()      #节点出队
        cur_depth = qd.popleft()    #深度出队
        if cur_depth > len(sum_of_level) - 1:  #当前深度尚无sum信息
            sum_of_level.append(cur_root.val)
        else :      #已有本层sum，则累加
            sum_of_level[cur_depth] += cur_root.val
        if cur_root.left != None :  #左子树入队
            q.append(cur_root.left)
            qd.append(cur_depth + 1)
        if cur_root.right != None :  #右子树入队
            q.append(cur_root.right)
            qd.append(cur_depth + 1)
    
    return sum_of_level[-1]



'''Input'''
root = makeTree([1,2,3,4,5,'null',6,7,'null','null','null','null',8])

'''
用队列实现层序遍历：先将根节点入队。每次循环，取出队列头的元素，进行访问处理，然后将其左右子树入队。
'''

'''Output'''
print(Solution(root))