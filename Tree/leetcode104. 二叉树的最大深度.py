'''
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
'''

# BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_error:
    def maxDepth(self, root: TreeNode) -> int:
        # 特殊情况：
        if root == None :
            return [] # 错误1 返回的应该是0 没有树那么应该是0层，不是一个空列表
        depth = 0
        queue = [root]
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop()
                # 错误2 第一个queue只有[root],len=1，循环1次，然后pop出来root剩[],加入[2,3],depth=1
                # len=2，循环两次，然后pop出来的是3不是2剩[3]，然后添加5，[2，5]那么在pop就是5，depth=2
                # 列表剩[2]，len=1，循环1次，pop出来2，剩[],加入4，剩[4],depth=3
                # len = 1 循环1次，pop出来4，剩[]，depth=4
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth +=1
        return depth

# 改错方法1，pop要注意顺序，pop(0)
class Solution1:
    def maxDepth(self, root: TreeNode) -> int:
        # 特殊情况：
        if root == None :
            return 0
        depth = 0
        queue = [root]
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth +=1
        return depth

# 改错方法2 设置一个tmp，用于存储下一层的节点，queue只存当前节点，这样就不用考虑pop位置
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 特殊情况：
        if root == None :
            return 0
        depth = 0
        queue = [root]
        while queue:
            size = len(queue)
            tmp = []
            for i in range(size):
                node = queue.pop()
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
            depth +=1
        return depth

# DFS
# 递归，左右子树最大深度+1，先走到底，然后在判断，然后逐步加1
class Solution3:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            depth = max(left_height, right_height) + 1
        return depth