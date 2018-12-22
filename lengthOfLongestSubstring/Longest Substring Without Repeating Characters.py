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
        d, a, m = {}, 0, 0
        for i, c in enumerate(s):
          if c in d and d[c] >= a:
            a = d[c] 
          m = max(m,  i - a)
          d[c] = i
        return m
            

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
    length = Solution().lengthOfLongestSubstring('abcdfa')
    print(length)