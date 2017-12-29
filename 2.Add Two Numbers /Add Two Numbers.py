#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        number1 = 0
        coefficient1 = 1
        while l1:
            number1 += coefficient1 * l1.val
            coefficient1 *= 10
            l1 = l1.next
        number2 = 0
        coefficient2 = 1
        while l2:
            number2 += coefficient2 * l2.val
            coefficient2 *= 10
            l2 = l2.next
        sum = number1 + number2
        if sum == 0:
            return ListNode(0)
        else:
            now = None
            front = None
            head = None
            while sum !=0:
                dig = sum % 10
                sum = sum // 10
                if front is None:
                    now = ListNode(dig)
                    head = now
                    front = now
                else:
                    now = ListNode(dig)
                    front.next = now
                    front = now
            return head

