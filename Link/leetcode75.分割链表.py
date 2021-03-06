'''
给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。
每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。
这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。
返回一个符合上述规则的链表的列表。

举例： 1->2->3->4, k = 5 // 5 结果 [ [1], [2], [3], [4], null ]

        示例 1：
        输入:
        root = [1, 2, 3], k = 5
        输出: [[1],[2],[3],[],[]]
        解释:
        输入输出各部分都应该是链表，而不是数组。
        例如, 输入的结点 root 的 val= 1, root.next.val = 2, \root.next.next.val = 3,
        且 root.next.next.next = null。
        第一个输出 output[0] 是 output[0].val = 1, output[0].next = null。
        最后一个元素 output[4] 为 null, 它代表了最后一个部分为空链表。

        示例 2：
        输入:
        root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
        输出: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
        解释:
        输入被分成了几个连续的部分，并且每部分的长度相差不超过1.前面部分的长度大于等于后面部分的长度。

'''
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        total_len = 0
        cur = root
        while cur:
            cur = cur.next
            total_len += 1
        length = total_len // k # 每一段的基础长度
        m = total_len % k # 前m段每段加一
        cur = root # 记得要恢复到原位
        res = []
        for i in range(k):
            res.append(cur) # 把每一小段的头节点添加进去
            size = length + (1 if m>0 else 0) # 计算每一段的真实长度
            if cur:
                for i in range(size - 1): # 刨除头节点后的长度
                    cur = cur.next
                # 注意缩进，如果在if 下面容易出现cur位空，没有next属性的情况
                m -= 1 # 记得每加一次都要把m-1
                # 断开链表
                tmp = cur.next # 设置一个指针标记下一段头节点
                cur.next = None
                cur = tmp
        return res