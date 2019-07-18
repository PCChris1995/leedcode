class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None 


class TreeNodeFun(object):
    def __init__(self):
        pass 
            
    def RebuildTree(self, pre_lst, mid_lst):
        """
        重建二叉树
        利用二叉树的前序遍历和中序遍历重建二叉树
        """
        if len(pre_lst) < 1:
            return None 
        val = pre_lst[0]
        root = TreeNode(val)
        index = mid_lst.index(val)
        root.left = self.RebuildTree(pre_lst[1:index+1], mid_lst[:index])
        root.right = self.RebuildTree(pre_lst[index+1:], mid_lst[index+1:])
        return root  

    def LeftestNode(self, head):
        """得到二叉树每行最左边的结点"""
        colum_list = []
        lst = []
        result = []
        lst.append(head)
        result.append([])
        while lst or colum_list:
            if not lst:
                result.append([])
                lst = colum_list
                colum_list = []
            node = lst.pop(0)
            if node.left:
                colum_list.append(node.left)
            if node.right != None:
                colum_list.append(node.right)
            result[-1].append(node.val)
        length = len(result)
        aa = []
        for i in range(length):
            aa.append(result[i][0])
        return aa 

    def list_2_tree(self, lst, index):
        """根据列表重建二叉树"""
        if index > len(lst) - 1:
            return None 
        node = TreeNode(lst[index])
        if 2*index+1 <= len(lst):
            node.left = self.list_2_tree(lst, 2*index+1)
        if 2*index+1+1 <= len(lst):
            node.right = self.list_2_tree(lst, 2*index+1+1)
        return node 

    def last_find(self, head, digui=True):
        """
        二叉树的后序遍历
        head: 头节点
        digui: 是否采用递归方法
        """
        if digui:
            if head:
                self.last_find(head.left)
                self.last_find(head.right)
                print(head.val)
        else:
            lst = []
            stack = []
            curr = head 
            while curr or stack:
                if curr:
                    lst.append(curr.val)
                    stack.append(curr.left)
                    curr = curr.right
                else:
                    curr = stack.pop()
            return lst[::-1]

    def mid_find(self, head, digui=True):
        """
        二叉树的中序遍历
        """
        if digui:
            if not head:
                return 
            self.mid_find(head.left)
            print(head.val)
            self.mid_find(head.right)
        else:
            lst = []
            stack = []
            curr = head 
            while curr or stack:
                if curr:
                    stack.append(curr)
                    curr = curr.left 
                else:
                    curr = stack.pop()
                    lst.append(curr.val)
                    curr = curr.right 
            return lst 

    def pre_find(self, head, digui=True):
        """
        二叉树的前序遍历
        """
        if digui:
            if not head:
                return 
            print(head.val)
            self.pre_find(head.left)
            self.pre_find(head.right)
        else:
            stack = []
            lst = []
            curr = head 
            while curr or stack:
                if curr:
                    lst.append(curr.val)
                    stack.append(curr.right)
                    curr = curr.left
                else:
                    curr = stack.pop()
            return lst 

    def Hierachy_find(self, head):
        """
        二叉树的层次遍历
        """
        lst = []
        stack = [head]
        while stack:
            curr = stack.pop(0)
            lst.append(curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return lst 


    def pre_sort(self, str1, str2):
        """
        利用中序遍历和后序遍历得到前序遍历
        str1: 后序遍历的list
        str2: 中序遍历的list
        """
        if len(str1) <= 1:
            return str1
        val = str1[-1]
        index = str2.index(val)
        return [val] + self.pre_sort(str1[:index], str2[:index]) + self.pre_sort(str1[index:-1], str2[index+1:]) 
        
    def mid_sort(self, str1, str2):
        """利用前序遍历和中序遍历得到中序遍历"""
        if len(str1) <= 1:
            return str1
        val = str1[0]
        index = str2.index(val)
        return self.mid_sort(str1[1:index+1], str2[:index]) + str1[0:1] + self.mid_sort(str1[index+1:], str2[index+1:])

    def last_sort(self, str1, str2):
        """利用二叉树的前序遍历和中序遍历重建二叉树"""
        if len(str2) <= 1:
            return str2
        else:
            return self.last_sort(str1[1:str2.index(str1[0])+1], str2[:str2.index(str1[0])]) \
                + self.last_sort(str1[str2.index(str1[0])+1:], str2[str2.index(str1[0])+1:]) + str1[0:1]


pre = ['A', 'B', 'D', 'C', 'E', 'F']
mid = ['D', 'B', 'A', 'E', 'C', 'F']
last = ['D', 'B', 'E', 'F', 'C', 'A']
aa = TreeNodeFun()
head  = aa.RebuildTree(pre, mid)
# print(pre_sort(last, mid))
print(aa.Hierachy_find(head))

