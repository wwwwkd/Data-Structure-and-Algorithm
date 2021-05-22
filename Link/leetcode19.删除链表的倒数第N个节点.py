'''
    给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
    进阶：你能尝试使用一趟扫描实现吗？
        示例 1：
        输入：head = [1,2,3,4,5], n = 2
        输出：[1,2,3,5]

        示例 2：
        输入：head = [1], n = 1
        输出：[]

        示例 3：
        输入：head = [1,2], n = 1
        输出：[1]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        思路1：
        （1）首先我们遍历一遍链表，得到链表的总长度count
        （2）然后将cur和pre遍历到相应位置count-n，此时cur所指向的位置就是我们要删除的倒数第n个节点。
        （3）设置dummy节点，防止删除第一个节点时报错
        '''
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head

        count = 0
        while count:
            cur = cur.next
            count += 1
        cur = head
        for i in range(count - n):
            pre = cur
            cur = cur.next
        pre.next = cur.next # 若删除的为第一个节点，pre为None，没有next方法，会报错，设置dummy
        return dummy.next

class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        思路2：
        （1）可以利用两个指针之间得间隔，当cur指向None即出界时，
        利用距离为n的节点之前的pre节点来完成这道题目，pre.next = pre. next.next
        （2）注意特殊情况，删除的为第一个节点时，这时我们要设置一个dummy节点
        '''
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        pre = dummy

        for i in range(n):
            cur = cur.next
        while cur:
            pre = pre.next
            cur = cur.next
        pre.next