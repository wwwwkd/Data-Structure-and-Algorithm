'''
    给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。
    将这两数相加会返回一个新的链表。你可以假设除了数字 0 之外，这两个数字都不会以零开头。

        进阶：
        如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

        示例：
        输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
        输出：7 -> 8 -> 0 -> 7
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    （1）这道题与上一道题的区别：上一道题的高位在链表的尾部，因此可以设定两个指针在链表头部按位遍历再相加。
    而本题的高位在尾部，要想先让尾部按位相加，可以利用栈的知识，先将两个链表由到尾压入栈中，栈的特性是先入后出，
    因此可以再出栈时按位相加。
    （2）两种特殊情况和上一题就一样了，循环的时候要判断是不是栈是否为空，是否还有进位。
    另一个就是，按位相加是三个数相加，x+y+carry
    （3）如何进行连接，设置dummy节点，新节点的.next指向dummy.next，而dummy.next永远指向头节点。
    '''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = [], []
        carry = 0
        dummy = ListNode(0)

        # l1入栈
        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        # l2入栈
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        while carry or stack1 or stack2:
            # l1不为空返回val，为空返回0
            if stack1:
                val1 = stack1.pop()
            else:
                val1 = 0

            # l2 同理
            if stack2:
                val2 = stack2.pop()
            else:
                val2 = 0

            # 当前位，余数，进位
            carry += val1 + val2
            valnode = carry % 10
            carry = carry // 10

            # 连接
            node = ListNode(valnode)
            node.next = dummy.next
            dummy.next = node
        return dummy.next
