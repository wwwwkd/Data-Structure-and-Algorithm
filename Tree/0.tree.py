'''
    1. 二叉树的结构有节点，但是他与链表不一样，Tree有左右两个next，并且像链表的头部一样，设置一个根节点 self.root = None
    2. 单独的一个节点没有指向，只有创建一个新的节点，并且放入到树中，才会有之后的指向，这与链表相似

'''
class Node():
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None

    # 构建二叉树
class Tree():
    def __init__(self):
        self.root = None

    def addNode(self, item):
        # 创建新的节点
        node = Node(item)
        # 特殊情况：无根节点，插入的是第一个节点的话
        if self.root == None:
            self.root = node
            return

        # 普通情况：插入的节点不是第一个节点
        cur = self.root
        q = [cur] # 将未遍历的节点放入列表

        while q: # 当遍历完所有列表中的元素，则停止循环
            nd = q.pop(0) # 去除第一个列表中未遍历的元素

            # 判断左叶子节点
            if nd.left == None:
                nd.left = node
                return
            else:
                q.append(nd.left)

            # 判断右叶子节点
            if nd.right == None:
                nd.right = node
                return
            else:
                q.append(nd.right)

    # 前序： 根左右
    def forward(self, root):
        # 特殊情况： 无根节点
        if root == None:
            return
        print(root.item)
        self.forward(root.left)
        self.forward(root.right)

    def forward_DFS(self, root):
        # 特殊情况： 如果树为空
        res = []
        def dfs(root):
            if root == None:
                return
            res.append(root.val)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
        dfs(root)
        return res

    def forward_BFS(self, root):
        if root == None:
            return []
        res = []
        stack = [root]
        # 栈的特性，先进后出，那么先进右子树，然后左子树，这样出就是左子树先出，达到前序遍历
        while stack:
            r = stack.pop()
            res.append(r.val)
            if r.right:
                stack.append(r.right)
            if r.left:
                stack.append(r.left)
        return res

    def forward_Ineration(self, root):
        stack = []
        res = []
        while stack or root:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return res

    # 中序： 左根右
    def middle(self, root):
        # 特殊情况： 无根节点
        if root == None:
            return
        self.middle(root.left)
        print(root.item)
        self.middle(root.right)

    def middle_Ineration(self, root):
        stack = []
        res = []
        while stack or root:
        # 1.stack = None root != None 根节点
        # 2.stack != None root = None遍历结束
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

    def middle_DFS(self, root):
        res = []
        def dfs(root):
            if root == None:
                return
            if root.left:
                dfs(root.left)
            res.append(root.val)
            if root.right:
                dfs(root.right)
        dfs(root)
        return res

    # 后序： 左右根
    def back(self, root):
        # 特殊情况： 无根节点zq
        if root == None:
            return
        self.middle(root.left)
        self.middle(root.right)
        print(root.item)




    def travel(self):
        cur = self.root
        q = [cur]
        while q:
            nd = q.pop(0)
            print(nd.item)
            if nd.left:
                q.append(nd.left)
            if nd.right:
                q.append(nd.right)

tree = Tree()
tree.addNode(1)
tree.addNode(2)
tree.addNode(3)
tree.addNode(4)
tree.addNode(5)
tree.addNode(6)
# tree.travel()

tree.addNode(7)
tree.travel()

