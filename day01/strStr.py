'''
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
'''
# 可以直接使用indexOf方法 直接搞定！！！

class Solution(object):
    # 思路1：双指针算法 时间复杂度 m*n
    def strStr1(self, haystack, needle):
        if len(needle) == 0:
            return 0
        if len(haystack) < len(needle):
            return -1
        i = 0
        j = 0
        index = -1
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                # 如果字符相等，则记录第一个相等字符的index
                if j == 0:
                    index = i
                # 如果所有字符都相等，直接返回index
                elif j == len(needle)-1:
                    print(index)
                    return index
                i += 1
                j += 1
            # 如果字符串不相等，则回到index+1的位置
            else:
                j = 0
                i = index + 1 if index != -1 else i + 1
                index = -1
        # 如果index大于二者之差，则返回-1
        if index > len(haystack) - len(needle):
            index = -1
        return index

    # 思路2：官方解法(这里直接用字符串切割并比较，而不是用每一个字符比较) 时间复杂度 (m-n)*n
    def strStr2(self, haystack, needle):
        L, n = len(needle), len(haystack)
        for start in range(n - L + 1):
            if haystack[start: start + L] == needle:
                return start
        return -1

    # 思路3：官方解法：双指针 - 线性时间复杂度(m-n)*n
    class Solution:
        def strStr3(self, haystack: str, needle: str) -> int:
            L, n = len(needle), len(haystack)
            if L == 0:
                return 0

            pn = 0
            # 这里限制了外层循环不超过 n-L+1
            while pn < n - L + 1:
                # find the position of the first needle character
                # in the haystack string
                # 寻找第一位相等的字符
                while pn < n - L + 1 and haystack[pn] != needle[0]:
                    pn += 1

                # compute the max match string
                # 记录当前匹配长度和子串指针
                curr_len = pL = 0
                # 寻找第二个及之后相等的字符
                while pL < L and pn < n and haystack[pn] == needle[pL]:
                    pn += 1
                    pL += 1
                    curr_len += 1

                # if the whole needle string is found,
                # return its start position
                # 如果完全匹配，则返回index
                if curr_len == L:
                    return pn - L

                # otherwise, backtrack
                pn = pn - curr_len + 1

            return -1

    # 思路4: 滚动hash

    # 思路5: KMP


if __name__=='__main__':
    s = Solution()
    s.strStr1("mississippi", "issipi")
