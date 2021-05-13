'''

    根据一棵树的前序遍历与中序遍历构造二叉树。

    注意:
    你可以假设树中没有重复的元素。

    例如，给出

    前序遍历 preorder = [3,9,20,15,7]
    中序遍历 inorder = [9,3,15,20,7]

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution1:
    '''
    前序遍历 preorder = [3,9,20,15,7]
    中序遍历 inorder = [9,3,15,20,7]
    我们可以发现：前序遍历的第一个元素为根节点，而在后序遍历中，该根节点所在位置的左侧为左子树，右侧为右子树。
    所以构建二叉树的问题本质上就是：
        1)找到各个子树的根节点 root
        2)构建该根节点的左子树
        3)构建该根节点的右子树
    '''
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 特殊情况： 树为空
        if len(preorder) == 0:
            return None
        # 前序遍历中的第一个元素应该是该树的根节点
        root = TreeNode(preorder[0])
        # 构建左子树
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # 构建右子树
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
