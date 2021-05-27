'''

    给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
    k 是一个正整数，它的值小于或等于链表的长度。
    如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
    进阶：
    你可以设计一个只使用常数额外空间的算法来解决此问题吗？
    你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

        示例 1：
        输入：head = [1,2,3,4,5], k = 2
        输出：[2,1,4,3,5]

        示例 2：
        输入：head = [1,2,3,4,5], k = 3
        输出：[3,2,1,4,5]

        示例 3：
        输入：head = [1,2,3,4,5], k = 1
        输出：[1,2,3,4,5]

        示例 4：
        输入：head = [1], k = 1
        输出：[1]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    思路：
    （1）链表分区为已翻转部分+待翻转部分+未翻转部分
    （2）每次翻转前，要确定翻转链表的范围，这个必须通过 k 此循环来确定
    （3）需记录翻转链表前驱和后继，方便翻转完成后把已翻转部分和未翻转部分连接起来
        初始需要两个变量 pre 和 end，pre 代表待翻转链表的前驱，end 代表待翻转链表的末尾
        经过k此循环，end 到达末尾，记录待翻转链表的后继 next = end.next
    （4）翻转链表，然后将三部分链表连接起来，然后重置 pre 和 end 指针，然后进入下一次循环
    （5）特殊情况，当翻转部分长度不足 k 时，在定位 end 完成后，end==null，
        已经到达末尾，说明题目已完成，直接返回即可
    '''
    def reverse(self, head):
        cur = head
        pre = None
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre, end = dummy, dummy
        start, next_i = head, head


        while next_i:
            i = 0
            # 移动end指针，
            if i<k and end:
                end = end.next
                i += 1
            if end == None: break # 如果end为空了那么直接跳出循环

            # 更新start，next_i指针
            start = pre.next # 当翻转第二段链表时，start还在上一段链表的末尾
            next_i = end.next

            # 断开链表
            end.next = None

            # 翻转链表
            pre.next = self.reverse(start)

            # 更新pre,end指针
            pre = start
            end = pre

        return dummy.next








