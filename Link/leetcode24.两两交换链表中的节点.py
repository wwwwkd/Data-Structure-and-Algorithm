'''
    给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
    你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

        示例 1：
        输入：head = [1,2,3,4]
        输出：[2,1,4,3]

        示例 2：
        输入：head = []
        输出：[]

        示例 3：
        输入：head = [1]
        输出：[1]
 '''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1:
    '''
    （1）n1 = p.next
    （2）n2 = p.next.next
    （3）p.next = n2
    （4）n1.next = n2.next
    （5）n2.next = n1
    （6）p = n1
    '''
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while pre.next and pre.next.next:
             n1 = pre.next
             n2 = pre.next.next
             pre.next = n2
             n1.next = n2.next
             n2.next = n1
             pre = n1 # 重置n1
        return dummy.next