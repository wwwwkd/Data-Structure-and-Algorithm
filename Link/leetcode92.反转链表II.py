'''
    给你单链表的头指针 head 和两个整数 left 和 right ，
    其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
         
        示例 1：
        输入：head = [1,2,3,4,5], left = 2, right = 4
        输出：[1,4,3,2,5]

        示例 2：
        输入：head = [5], left = 1, right = 1
        输出：[5]

        提示：

            链表中节点数目为 n
            1 <= n <= 500
            -500 <= Node.val <= 500
            1 <= left <= right <= n
'''
class Solution:
    '''
    （1）可以想象两边变为三部分，前一部分，反转部分，后一部分，反转m到n之间的链表
    （2）将反转好的链表与前后两部分进行拼接，设置两个站点，方便拼接
    （3）当没有前一部分，即m=1时，pre1 = None那么此是头节点直接等于pre
    '''
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        cur = head
        pre = None
        next_node = cur.next

        for i in range(left - 1):
            pre = cur
            cur = next_node
            if cur:
                next_node = cur.next

        pre1 = pre
        cur1 = cur

        for j in range(right - left + 1):
            cur.next = pre
            pre = cur
            cur = next_node
            if cur:
                next_node = cur.next

        if pre1 != None:
            pre1.next = pre
        else: # left = 1
            head = pre

        cur1.next = cur
        return  head

