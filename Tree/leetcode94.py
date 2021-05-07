'''
    给定一个二叉树的根节点 root ，返回它的 中序 遍历。
示例 1：
输入：root = [1,null,2,3]
输出：[1,3,2]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]

示例 4：
输入：root = [1,2]
输出：[2,1]

示例 5：
输入：root = [1,null,2]
输出：[1,2]

提示：
树中节点数目在范围 [0, 100] 内 -100 <= Node.val <= 100

进阶: 递归算法很简单，你可以通过迭代算法完成吗
'''


class Solution1:
    '''
        输入：[1,null,2,3] 输出：[1]
        p = [] 为局部变量，每一次递归都会更新为空列表
        self.inorderTraversal(root.left) 这么递归没有返回p的值，并且没有变量接收
    '''
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        p = []
        # 特殊情况：无根节点
        if root == None:
            return p
        # 递归
        self.inorderTraversal(root.left)
        p.append(root.val)
        self.inorderTraversal(root.right)
        return p

p = []
class Solution2:
    '''
        测试用例：1输入：[1,null,2,3] 输出：[1，3，2]
                 2输入：[] 输出：[1，3，2]
        p = [] 为全局变量，因此执行下一个例子时，
        调用Solution类中的方法inorderTraversal由于p内有元素无法清空，因此不能提交
    '''
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        # 特殊情况：无根节点
        if root == None:
            return p
        # 递归
        self.inorderTraversal(root.left)
        p.append(root.val)
        self.inorderTraversal(root.right)
        return p


class Solution3:
    '''
        正确答案
        我们可以写个for 然后更新列表
    '''
     def inorderTraversal(self, root: TreeNode) -> List[int]:
        p = []
        # 特殊情况： 无根节点的情况
        if root == None:
            return p
        l = self.inorderTraversal(root.left)
        for i in l:
            p.append(i)
        p.append(root.val)
        r = self.inorderTraversal(root.right)
        for j in r:
            p.append(j)
        return p




class Solution4:
    '''
        正确答案
        self.res = [] 为全局变量
        使用两个函数，使列表更新
    '''

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, root: TreeNode):
        if root == None:
            return self.res
        self.dfs(root.left)
        self.res.append(root.val)
        self.dfs(root.right)

