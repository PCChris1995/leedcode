class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None 


def RebuildTree(pre_lst, mid_lst):
    """
    重建二叉树
    利用二叉树的前序遍历和中序遍历重建二叉树
    """
    if len(pre_lst) < 1:
        return None 
    val = pre_lst[0]
    root = TreeNode(val)
    index = mid_lst.index(val)
    root.left = RebuildTree(pre_lst[1:index+1], mid_lst[:index])
    root.right = RebuildTree(pre_lst[index+1:], mid_lst[index+1:])
    return root  



def last_find(head, digui=True):
    """
    二叉树的后序遍历
    head: 头节点
    digui: 是否采用递归方法
    """
    if digui:
        if head:
            last_find(head.left)
            last_find(head.right)
            print(head.val)
    else:
        pass 


def pre_find(head):
    """
    二叉树的前序遍历
    """
    stack = []
    lst = []
    lst.append(head.val)
    stack.append(head)
    while stack:
        cur = stack.pop()
        lst.append(cur.val)
        stack.append(cur.left)
        




def pre_sort(str1, str2):
    """
    利用中序遍历和后序遍历得到前序遍历
    str1: 后序遍历的list
    str2: 中序遍历的list
    """
    if len(str1) <= 1:
        return str1
    val = str1[-1]
    index = str2.index(val)
    return [val] + pre_sort(str1[:index], str2[:index]) + pre_sort(str1[index:-1], str2[index+1:]) 
    


def mid_sort(str1, str2):
    """利用前序遍历和中序遍历得到中序遍历"""
    if len(str1) <= 1:
        return str1
    val = str1[0]
    index = str2.index(val)
    return mid_sort(str1[1:index+1], str2[:index]) + str1[0:1] + mid_sort(str1[index+1:], str2[index+1:])


def last_sort(str1, str2):
    """利用二叉树的前序遍历和中序遍历重建二叉树"""
    if len(str2) <= 1:
        return str2
    else:
        return last_sort(str1[1:str2.index(str1[0])+1], str2[:str2.index(str1[0])]) \
            + last_sort(str1[str2.index(str1[0])+1:], str2[str2.index(str1[0])+1:]) + str1[0:1]


pre = ['A', 'B', 'D', 'C', 'E', 'F']
mid = ['D', 'B', 'A', 'E', 'C', 'F']
last = ['D', 'B', 'E', 'F', 'C', 'A']
# root = RebuildTree(pre, mid)
print(pre_sort(last, mid))

