# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 13:36:26 2021

@author: catal
"""
from typing import NewType


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


ListNode = NewType('ListNode', int)


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    """assumes l1 and l2 are ListNode objects
    returns a ListNode object, the sum of l1 and l2"""
    # find larger ListNode
    if len(l1) <= len(l2):
        smaller_listNode = l1
        larger_listNode = l2
    else:
        smaller_listNode = l2
        larger_listNode = l1

    # initialize variable
    l3 = []
    carry_over = False

    # iterate over nodes
    for count, node in enumerate(larger_listNode):
        try:
            node_sum = l1[count]+l2[count]
        except IndexError:
            node_sum = larger_listNode[count]
        if carry_over:
            node_sum += 1
            carry_over = False
        if node_sum > 9:
            carry_over = True
            l3.append(int(str(node_sum)[1]))
        else:
            l3.append(node_sum)
    if carry_over:
        l3.append(1)

    return l3


l1 = [2, 4, 3]
l2 = [5, 6, 4]
l3 = [9, 9, 9, 9, 9, 9, 9]
l4 = [9, 9, 9, 9]
l5 = [2, 4, 3, 5]

# print(addTwoNumbers(l1, l2))  # expected [7, 0, 8]
# print(addTwoNumbers(l2, l5))
print(addTwoNumbers(l3, l4))  # expected [8, 9, 9, 9, 0, 0, 0, 1]
