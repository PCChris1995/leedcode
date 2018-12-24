# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 16:27:47 2018

@author: pchen
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
#        str_dict = dict()
#        begin = 0
#        max_len = 0
#        for index, str1 in enumerate(s):
#            if str1 in str_dict and index > begin:
#                begin = index
#            str_dict[str1] = index
#            max_len = max(max_len, index+1-begin)
#        return max_len
        dict1 = {}
        result = 0
        for index, letter in enumerate(s):
            if letter in dict1:
                a = dict1[letter]
                num = index - a
                if result < num:
                    result = num
                    str1 = s[a:index]
            dict1[letter] = index
        return result, str1
            

def stringToString(input):
    import json

    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line);
            
            ret = Solution().lengthOfLongestSubstring(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    length, str1 = Solution().lengthOfLongestSubstring('adgatadf')
    print(length, str1)