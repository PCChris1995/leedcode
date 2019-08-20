# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 16:27:26 2018
"""链表相关代码"""
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

def link_quick_sort(node):
  """链表快排"""
  def part(pbegin, pend):
    val = pbegin.val
    p = pbegin 
    q = p.next 
    while q:
      if q.val < val:
        p = p.next 
        p.val, q.val = q.val, p.val
      q = q.next 
    p.val, pbegin.val = pbegin.val, p.val 
    return p

  def quick_sort(pbegin, pend):
    if pbegin != pend:
      partition = part(pbegin, pend)
      quick_sort(pbegin, partition)
      quick_sort(partition.next, pend)
  quick_sort(node, None)
  return node 


class Solution:
    """不交换值的链表快排"""
    def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        leftH = ListNode(0)
        resL = leftH
        rightH = ListNode(0)
        resR = rightH
        midNode = head
        head = head.next
        while head != None:
            if head.val < midNode.val:
                leftH.next = head
                leftH = leftH.next
            else:
                rightH.next = head
                rightH =rightH.next
            head = head.next
        leftH.next = None
        rightH.next = None
        L = self.sortList(resL.next)
        R = self.sortList(resR.next)
        midNode.next = R
        if L == None:
            return midNode
        tmp = L
        while tmp.next != None:
            tmp = tmp.next
        tmp.next = midNode
        return L

l1 = ListNode(0)    
ListNode_1 = ListNode_handle()
l1 = ListNode(0)
l1_list = [1,8,3]
for i in l1_list:
    ListNode_1.add(i)

ListNode_1.print_ListNode()
