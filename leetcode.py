class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        https://leetcode-cn.com/problems/string-to-integer-atoi/
        """
        flag = ['1', '-', ' ', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+']
        number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        if str == "" or str[0] not in flag:
            return 0
        i = 0
        while i < len(str) and str[i] == ' ':
            i += 1
        if i >= len(str) or str[i] not in flag:
            return 0
        positve_flag = True

        if str[i] == '-' or str[i] == '+':
            if str[i] == '-':
                positve_flag = False 
            i = i + 1
        if i >= len(str) or str[i] not in number:
            return 0
        j = i
        while j < len(str):
            if str[j] not in number:
                break 
            j += 1
        res = int(str[i:j])
        over = (1 << 31) - 1
        if res > over: # handle the overflow
            res = over if positve_flag else over + 1
        return res if positve_flag else -res

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        https://leetcode-cn.com/problems/3sum/
        """
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            first = i + 1
            last = len(nums) - 1
            while first < last:
                if nums[i] + nums[first] + nums[last] == 0:
                    res.append([nums[i], nums[first], nums[last]])
                    while first < last and nums[first] == nums[first+1]:
                        first += 1
                    while first < last and nums[last] == nums[last-1]:
                        last -= 1
                    last -= 1
                    first += 1
                while first < last and nums[i] + nums[first] + nums[last] > 0:
                    last -= 1
                while first < last and nums[i] + nums[first] + nums[last] < 0:
                    first += 1
        return res

    def all_sort(self, str, start , end):
        """
        字符串的全排列
        """
        """
        # DFS的递归方法
        # str = list(str)
        if start == end:
            result = "".join(str)
            print(result)
            return 
        for i in range(start, end+1):
            str[i], str[start] = str[start], str[i]
            self.all_sort(str, start+1, end)
            str[i], str[start] = str[start], str[i]
        """
        # BFS的非递归方法
        res = ['']
        for _ in str:
            next_res = []
            for tmp1 in res:
                for tmp in str:
                    if tmp in tmp1:
                        continue
                    next_res.append(tmp1+tmp)
            res = next_res
        return res



    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
        """
        """
        # DFS的递归版本
        if len(digits) <= 0:
            return []
        
        lookup = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        length = len(digits)
        result = []
        def helper(i, string):
            if i == length:
                result.append(string)
                return 
            for char in lookup[digits[i]]:
                helper(i+1, string+char)
        
        helper(0, "")
        return result
        """
        # 非递归版本的BFS
        if len(digits) <= 0:
            return []
        
        lookup = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = ['']
        for num in digits:
            next_res = []
            for char in lookup[num]:
                for tmp in res:
                    next_res.append(tmp + char)
            res = next_res
        return res


    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        for i in range(len(s)):
            if i > 0 and a[s[i]] > a[s[i-1]]:
                ans += a[s[i]]
                ans -= 2*a[s[i-1]]
            else:
                ans += a[s[i]]
        return ans


    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
        """
        cur = head
        for i in range(n+1):
            cur = cur.next
            if not cur:
                if i == n:
                    return head.next
                else:
                    head.next = head.next.next
                    return head
        first = cur 
        last = head 
        while first:
            first = first.next 
            last = last.next 
        last.next = last.next.next
        return head

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1 
        for j in range(1, len(nums)):
            if nums[j] == nums[i]:
                continue
            i += 1
            nums[i] = nums[j]
        return i

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        https://leetcode-cn.com/problems/implement-strstr/
        """
        if needle not in haystack:
            return -1
        if len(needle) == 0 and len(haystack) != 0:
            return 0
        for i in range(len(haystack)-len(needle) + 1):
            if needle[0] != haystack[i]:
                continue
            if needle == haystack[i:i+len(needle)]:
                return i
        return 0

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        https://leetcode-cn.com/problems/divide-two-integers/
        """
        end_flag = True
        sor_flag = True
        if dividend < 0:
            end_flag = False
            dividend = -dividend
        if divisor < 0:
            sor_flag = False
            divisor = -divisor
        res = 0
        while dividend >= divisor:
            tmp, i = divisor, 1
            while dividend >= tmp:
                dividend -= tmp
                res += i
                tmp <<= 1
                i <<= 1
        neg_flag = True if end_flag != sor_flag else False
        res = -res if neg_flag else res
        return min(max(-2**31, res), 2**31-1)

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        https://leetcode-cn.com/problems/valid-sudoku/
        perfect solution:https://leetcode-cn.com/problems/valid-sudoku/solution/you-xiao-de-shu-du-by-leetcode/
        """
        def is_double(lst):
            hash = []
            for val in lst:
                if val == '.':
                    continue
                if val in hash:
                    return True
                hash.append(val)
            return False            

        for i in range(len(board)):
            if is_double(board[i]):
                return False
        
        for i in range(len(board[0])):
            lst = []
            for j in range(len(board)):
                lst.append(board[j][i])
            if is_double(lst):
                return False
        
        lst = []
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                lst.extend(board[i][j:j+3])
                lst.extend(board[i+1][j:j+3])
                lst.extend(board[i+2][j:j+3])
                if is_double(lst):
                    return False
                lst = []
        return True 
                
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def read_num(last):
            """
            输入上一个数
            return: 上一个数的读数
            """
            result = ''
            duble = 1
            for i in range(1, len(last)):
                if last[i] != last[i-1]:
                    result += str(duble)
                    result += str(last[i-1])
                    duble = 1
                else:
                    duble += 1
            result += str(duble)
            result += str(last[-1])
            return result

             
        n -= 1
        hash = []
        hash.append('1')
        for i in range(1, n+1):
            hash.append(read_num(hash[i-1]))
        return hash[-1]

    
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        https://leetcode-cn.com/problems/4sum/
        """
        nums.sort()
        result = []
        n = len(nums)
        for i in range(len(nums) -3):
            # if nums[i] == nums[i+1]:
            #     continue
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            for j in range(i+1, n-2):
                # if nums[j] == nums[j+1]:
                #     continue
                if nums[j] + nums[n-1] + nums[n-2] + nums[i] < target:
                    continue
                if nums[j] + nums[j+1] + nums[j+2] + nums[i] > target:
                    break

                left = j + 1
                right = n - 1

                sum = target - nums[i] - nums[j]
                while left < right:
                    if nums[left] + nums[right] == sum:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    while left < right and nums[left] + nums[right] < sum:
                        left += 1
                    while left < right and nums[left] + nums[right] > sum:
                        right -= 1
        return result 

    
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        if nums == []:
            return 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j 

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        https://leetcode-cn.com/problems/add-strings/
        """
        len1 = len(num1)-1
        len2 = len(num2)-1
        carry = 0
        res = ''
        while len1 >= 0 or len2 >= 0:
            n1 = ord(num1[len1]) - ord('0') if len1 >= 0 else 0
            n2 = ord(num2[len2]) - ord('0') if len2 >= 0 else 0
            tmp = n1 + n2 + carry 
            carry = tmp // 10
            res += str(tmp % 10)
            len1, len2 = len1-1, len2-1
        if carry: return '1' + res
        return res 
            
        



if __name__ == "__main__":
    aa = Solution()
    # lists = [0, 0, 0, 0]
    # result = aa.threeSum(lists)
    # result = aa.all_sort(list('adc'), 0 , 2)
    # result = aa.letterCombinations('23')
    # result = aa.strStr("mississippi","pi")
    input = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    # result = aa.isValidSudoku(input)
    # result = aa.countAndSay(3)
    # lst = [-1,0,1,2,-1,-4]
    # result = aa.fourSum(lst, -1)
    result = aa.addStrings('1234', '23535')
    print(result)
        