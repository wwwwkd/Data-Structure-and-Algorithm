'''
    将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

        示例 1：
        输入：l1 = [1,2,4], l2 = [1,3,4]
        输出：[1,1,2,3,4,4]

        示例 2：
        输入：l1 = [], l2 = []
        输出：[]

        示例 3：
        输入：l1 = [], l2 = [0]
        输出：[0]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1:
    '''
    递归法：
    （1）终止条件：当l1和l2有一个为空停止迭代
    （2）如何递归：若l1.val<l2.val,那么l1.next = self.mergeTwoLists(l1.next,l2) return l1
    '''
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

class Solution2:
    '''
    迭代法：
    （1）我们设定一个哨兵节点 prehead ，这可以在最后让我们比较容易地返回合并后的链表。
        我们维护一个 prev 指针，我们需要做的是调整它的 next 指针。然后，我们重复以下过程，
        直到 l1 或者 l2 指向了 null ：如果 l1 当前节点的值小于等于 l2 ，
        我们就把 l1 当前的节点接在 prev 节点的后面同时将 l1 指针往后移一位。
        否则，我们对 l2 做同样的操作。不管我们将哪一个元素接在了后面，我们都需要把 prev 向后移一位。
    （2）在循环终止的时候， l1 和 l2 至多有一个是非空的。
    '''
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(0)
        prev = prehead

        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 if l1 is not None else l2
        return prehead.next