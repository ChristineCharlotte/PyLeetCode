"""
@Time    : 2022/7/4 14:17
@Author  : 刘俊 jun.liu@deepfinance.com
@File    : 3.py
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == ' ':
            return 0
        str_set = set()
        longestLength = 0

        # 起始指针所在位置
        for start in range(len(s)):
            str_set.clear()
            # i 代表 字符在 s 中的索引
            for i in range(len(s) - start):
                if s[start + i] in str_set:
                    if longestLength < i - start + 1:
                        longestLength = i - start
                    break
                else:
                    str_set.add(s[i])

        return longestLength
