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
    # goal = sum 2 linked lists
    # left most digit = least significant
    # right most digit = most significant
    # plan: take larger listnode
    # for node in listnode:
    #     l3 = l1 + l2[1]
    #     if l3 > 9:
    #         carry_over = l3[0]
    pass


l1 = [2, 4, 3]
l2 = [5, 6, 4]
addTwoNumbers(l1, l2)  # expected [7, 0, 8]
