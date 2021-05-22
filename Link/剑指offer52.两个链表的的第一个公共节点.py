'''
编写一个程序，找到两个单链表相交的起始节点。
如下面的两个链表：

输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，
链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，
相交节点前有 3 个节点。

常规思路
（1）先固定一个节点如headA
（2）headB遍历一遍，虽然A得4和B得4值相同但是不是一个引用。B遍历完成之后，A走下一个，B在遍历一圈。直到A和B得节点重合
（3）这是一个双循环，时间复杂度为O(n^2)
'''
'''
思路：
（1）根据链表得特性我们可以知道，如果两个链表有公共节点是不可能出现以下情况得，因为每个节点，只有一个next。
（2）要求时间复杂度为 O(N)，空间复杂度为 O(1)。如果不存在交点则返回 null。
（3）设 A 的长度为 a + c，B 的长度为 b + c，其中 c 为尾部公共部分长度，可知 a + c + b = b + c + a。
（4）当访问 A 链表的指针访问到链表尾部时，令它从链表 B 的头部开始访问链表 B；同样地，
     当访问 B 链表的指针访问到链表尾部时，令它从链表 A 的头部开始访问链表 A。
     这样就能控制访问 A 和 B 两个链表的指针能同时访问到交点。
（5）如果不存在交点，那么 a + b = b + a，以下实现代码中 node1 和 node2 会同时为 null，从而退出循环。
（6）单次循环，复杂度为O(n)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA
        return node1