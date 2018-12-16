# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 16:27:26 2018

@author: pengchen
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNode_handle:
    def __init__(self):
        self.cur_node = None
        self.node = ListNode(0)
        self._head = ListNode(None)
        
    def add(self, data):
        #add a new node pointed to previous node
        node = ListNode(0)
        node.val = data
        node.next = self._head
        self._head = node
        return node
    
    def append(self, data): 
        node = ListNode(data)
        header = self._head
        while header.next is not None:
            header = header.next
        header.next = node
 
    def print_ListNode(self):
        node = self._head
        while node:
            print('\nnode: ', node, ' value: ', node.val, ' next: ', node.next)
            node = node.next
 
    def _reverse(self, nodelist):
        list = []
        while nodelist:
            list.append(nodelist.val)
            nodelist = nodelist.next
        result = ListNode()
        result_handle = ListNode_handle()
        for i in list:
            result = result_handle.add(i)
        return result

       
class Solution:
    def addTwoNumbers(l1, l2):
        ret = l1.val + l2.val
        if ret > 9:
            c = 1
            ret = ret - 10
        tt = ListNode(ret)
        while l1.next != None or l2.next != None or c != 0:
            l1 = l1.next
            l2 = l2.next
            tt.next = l1.next + l2.next + c
        return ret

def add_test(header, data): 
    node = ListNode(data)
    while header.next is not None:
        header = header.next
    header.next = node
    return header

l1 = ListNode(0)    
ListNode_1 = ListNode_handle()
l1 = ListNode(0)
l1_list = [1,8,3]
for i in l1_list:
    ListNode_1.add(i)

ListNode_1.print_ListNode()
