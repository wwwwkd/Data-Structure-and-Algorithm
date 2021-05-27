'''
    请判断一个链表是否为回文链表。

    示例 1:
    输入: 1->2
    输出: false

    示例 2:
    输入: 1->2->2->1
    输出: true

    进阶：
    你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        '''
        分析：
        （1）空间复杂度位O（1）所以不能开辟新的内存
        （2）设置快慢指针，截取链表
        （3）链表反转，并一一比较
        '''
        slow = head
        fast = head
        # 截取链表
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 反转链表
        cur = slow
        pre = None
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node

        # 一一对比
        while pre and head:
            if pre.val != head.val:
                return False
            pre = pre.next
            head = head.next
        return True

