'''
    存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。
    返回同样按升序排列的结果链表。

        示例 1：
        输入：head = [1,1,2]
        输出：[1,2]

        示例 2：
        输入：head = [1,1,2,3,3]
        输出：[1,2,3]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1:
    '''
    递归法：
    （1）终止条件：当整个链表都没有重复节点时结束。
    （2）如何递归：当头节点或者下一个节点不为空时，则调用函数排除重复节点。
    （3）头节点之后的节点都是没有重复节点的链表，因此，如果头节点点与下一个节点val相同，则返回head.next。
    '''
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        head.next = self.deleteDuplicates(head.next)
        if head.val == head.next.val:
            return head.next
        else:
            return head
class Solution2:
    '''
    迭代法：
    （1）终止条件：cur 或者 cur.next 为None。
    '''
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head