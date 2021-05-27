'''
    给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，
    并且每个节点只能存储 一位 数字。请你将两个数相加，并以相同形式返回一个表示和的链表。
    你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

        示例 1：
        输入：l1 = [2,4,3], l2 = [5,6,4]
        输出：[7,0,8]
        解释：342 + 465 = 807.

        示例 2：
        输入：l1 = [0], l2 = [0]
        输出：[0]

        示例 3：
        输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
        输出：[8,9,9,9,0,0,0,1]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    （1）注意长度不同的两个数进行相加，且对应位相加的时候是三个数相加，x+y+carry
    （2）注意需要进位的情况，答案比原来的数要多一位 如 11 + 99 = 110，
        因此当任何一个数组没有遍历完或者有进位carry的情况，循环继续。
    （3）时间复杂度：O(max(m, n))，假设 m 和 n 分别表示 l1 和 l2 的长度，
        上面的算法最多重复 O(max(m, n)) 次。
    （4）空间复杂度：O(max(m, n))， 新列表的长度最多为 O(max(m, n))+1。
    '''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = tail = ListNode(0)
        carry = 0
        while l1 or l2 or carry: # 当l1,l2，或者有进位carry则循环不能停止
            carry = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0) # 计算当前位的和
            tail.next = ListNode(carry % 10) # 只要当前位的余数
            tail = tail.next # 记录
            carry //= 10 # 更新进位
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
