'''
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
叶节点是没有子节点的节点。

输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]
'''

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



class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def work(root,sum,path):  #当前节点root，当前和与路径（不包含root）为sum、path
            nonlocal targetSum
            if root.left == None and root.right == None :  #到达叶节点
                if sum + root.val == targetSum :
                    res.append(path+[root.val])
                    return
            if root.left != None :
                work(root.left, sum + root.val, path + [root.val])
            if root.right != None :
                work(root.right, sum + root.val, path + [root.val])


        res = []
        if not root :
            return []
        work(root,0,[])
        return res

'''解题区域'''

root = makeTree([5,4,8,11,'null',13,4,7,2,'null','null',5,1])
targetSum = 22
print(Solution().pathSum(root, targetSum))