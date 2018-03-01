#coding=utf-8


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        str1 = "".join([str(i) for i in list(reversed(convert(l1)))])
        str2 = "".join([str(i) for i in list(reversed(convert(l2)))])
        sum = int(str1) + int(str2)
        return list(reversed([int(s) for s in str(sum)]))


def convert(node):
    l = []
    while node:
        l.append(node.val)
        node = node.next
    return l
