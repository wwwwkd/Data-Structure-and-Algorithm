'''
    给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
    示例：
        二叉树：[3,9,20,null,null,15,7],
            3
           / \
          9  20
            /  \
           15   7
        返回其层序遍历结果：
        [
          [3],
          [9,20],
          [15,7]
        ]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
BFS （广度优先搜索）
    广度优先遍历是按层层遍历，遍历每一层的节点，题目要求返回每一层的节点值，所以题解1使用广度优先遍历
    广度优先遍历需要队列作为辅助结构，我们先将根节点放在队列中，然后不断遍历队列。
    首先拿出根节点，如果左右子树不为空，我们就将其放入队列中，经过第一遍处理之后，根节点已经从队列中拿走了，而根节点的两个孩子在队列中
    时间复杂度：O(n)
    空间复杂度：O(n)
'''
class Solution1:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 特殊情况：树为空
        if root == None:
            return []
        res = [] # 用于返回最终结果
        queue = [root] # 存放根节点
        while queue: # 若队列为空则停止遍历
            size = len(queue)
            tmp = [] # 存放临时列表，并将其添加到最终的列表res中
            for _ in range(size):
                root = queue.pop(0)
                tmp = tmp.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            res.append(tmp)
        return res


'''
DFS （深度优先搜索）
    每次一条路走到黑，root层级为0，就把root加到res中0位置[[3]]
    左子节点为9，层级为1，就把9加到res中1位置[[3],[9]]
    每次递归的时候都需要带一个 index(表示当前的层数)，如果当前行对应的list不存在，就加入一个空list进去，
    就像是[[3]],要把第二层的9加进去，当前的index > len(res)-1,就先加[[3],[]],然后在加9。
    时间复杂度：O(N)
    空间复杂度：O(h)，h是树的高度
'''

class Solution2:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        res = []
        def dfs(index, r):
            # 若当前层数在res中没有，就添加一个空list
            if index > len(res) - 1:
                res.append([])
            res[index].append(r.val)
            if r.left:
                dfs(index + 1, r.left)
            if r.right:
                dfs(index + 1, r.right)
        dfs(0, root)
        return res
