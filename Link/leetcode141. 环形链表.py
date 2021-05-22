'''
给定一个链表，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，
我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos
不作为参数进行传递，仅仅是为了标识链表的实际情况。
如果链表中存在环，则返回 true 。 否则，返回 false 。
示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

示例2：
输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
'''

'''
分析题目：题目要求我们判断他是否是环形链表。而不是说让我们根据pos连接环形链表。
首先我们设置一个快指针和一个慢指针slow，慢指针fast每次走一个，快指针每次走两个，当链表不是环形，那么fast最快走到链表尾部或者出界，那么代表不是环形链表。
然后，假如是环形链表，假如slow差一步，那么下次迭代相遇，若差两步以上，下下次跌倒也会相遇。
设置头节点为slow，头节点的下一个节点是fast，设置不一样的原因是，下面循环终止的条件是当fast = slow
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        find = False
        if slow == None or slow.next == None:
            return find
        fast = head.next
        while slow != fast :
            if fast == None or fast.next == None:
                return find
            slow = slow.next
            fast = fast.next.next
        find = True
        return  find