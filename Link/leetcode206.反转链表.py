'''
    给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

        示例 1：
        输入：head = [1,2,3,4,5]
        输出：[5,4,3,2,1]

        示例 2：
        输入：head = [1,2]
        输出：[2,1]

        示例 3：
        输入：head = []
        输出：[]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1:
    '''
    思路：
    (1)：设置3指针，pre，cur和next_node
    (2)：实现局部反转，cur.next = pre
    (3)：然后对指针进行跟新，让3个指针向前移动一位
    (4)：特殊情况：当没有节点是要进行判断。
        当进行next_node更新时候也要进行判断，若cur = None 时 next_node = cur.next 则会报错。
    '''

    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        pre = None
        cur = head
        next_node = cur.next
        while cur:
            cur.next = pre
            pre = cur
            cur = next_node
            if cur:
                next_node = cur.next
        head = pre
        return head

class Solution2:
    '''
    递归思路：
    (1)：设置终止条件。
    (2)：形成一个环，然后在断开环
    '''

    def reverseList(self, head: ListNode) -> ListNode:
        # 终止条件
        if head == None or head.next == None:
            return head
        # 递归
        head_node = self.reverseList(head.next)

        head.next.next = head
        head.next = None
        return head_node

class Solution3:
    '''
    一个指针
    '''

    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        while head:
            node = ListNode(head.val)
            node.next = pre
            pre = node
            head = head.next
        return pre
