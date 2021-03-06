'''
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。传入函数的唯一参数为 要被删除的节点 。

现有一个链表 -- head = [4,5,1,9]，它可以表示为:

示例 1：
输入：head = [4,5,1,9], node = 5
输出：[4,1,9]
解释：给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.

示例 2：
输入：head = [4,5,1,9], node = 1
输出：[4,5,9]
解释：给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.

'''



class Solution:
    def deleteNode(self, node):
        '''
        分析题目：
        首先一定要审清题，由于我们只知道要删除的节点，和该节点之后的节点，
        所以不能够使用node之前的节点next指向node之后的节点。
        然后分析，我们可以让node这个节点的值等于后一个节点的值，
        然后node.next = node.next.next，即可将后一个节点删除，完成题目要求。
        '''
        node.val = node.next.val
        node.next = node.next.next

