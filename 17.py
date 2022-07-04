"""
@Time    : 2022/7/4 15:30
@Author  : 刘俊 jun.liu@deepfinance.com
@File    : 17.py
"""

match = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}


class Solution:
    def cal_combnination(self, arr1, arr2):
        res = []
        if len(arr1) == 0 :
            return arr2
        for a1 in arr1:
            for a2 in arr2:
                res.append(a1 + a2)
        return res

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        res = []
        for v  in digits:
            res = self.cal_combnination(res, match[v])
        return res