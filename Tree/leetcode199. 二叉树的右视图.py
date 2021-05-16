'''
    给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

    示例:
    输入: [1,2,3,null,5,null,4]
    输出: [1, 3, 4]
    解释:

       1            <---
     /   \
    2     3         <---
     \     \
      5     4       <---
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
# 初步想法广度优先搜索，遍历每一层，将每一层最后一个节点的值保存在res中

class Solution_error:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        res = [root]
        queue = [root]
        while queue:
            size = len(queue)
            tmp = []
            for i in range(size):
                r = queue.pop()
                if r.left:
                    tmp.append(r.left)
                if r.right:
                    tmp.append(r.right)
            queue = tmp # 并没有赋值，只是将tmp的指针付给了queue本质上是指向同一块内存
            res.append(tmp.pop()) # 所以pop之后都会少元素
        return res


class Solution1:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        res = []
        queue = [root]
        while queue:
            tmp = []
            size = len(queue)
            res.append(queue[-1].val)
            # 这句话为啥不能放在下面，是因为遍历到最后一层之后queue没有元素为空，所以会超出索引值
            for i in range(size):
                r = queue.pop(0)
                if r.left:
                    tmp.append(r.left)
                if r.right:
                    tmp.append(r.right)
            queue = tmp
        return res

class Solution2:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:
            return  []
        res = []
        queue = [root]
        while queue:
            tmp = []
            size = len(queue)
            for i in range(size):
                r = queue.pop(0)
                if r.left:
                    tmp.append(r.left)
                if r.right:
                    tmp.append(r.right)
                if i == size-1: # size是这一层的元素个数，当i=size-1时就说明遍历到这一层最后一个元素
                    res.append(r.val)
            queue = tmp
        return res