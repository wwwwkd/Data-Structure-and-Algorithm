'''
给定一个二叉树，返回它的 后序 遍历。
示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3
输出: [3,2,1]
'''

# DFS
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 特殊情况： 如果树为空
        if root == None:
            return []
        res = []
        def dfs(root):
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            res.append(root.val)
        dfs(root)
        return res

# 迭代法
class Solution1:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, stack= [], []
        prev = None # 标记
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 与前序和中序模板多了一个判断过程，节点没有右孩子或者已经访问过该节点的子节点
            if not root.right or root.right == prev:
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right
        return res