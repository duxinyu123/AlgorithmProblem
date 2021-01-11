class Solution:
    def __init__(self):
        self.NEXT = []
        self.res = -1

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:  # 当模式串为空时，总能匹配成功
            return 0
        elif not haystack:  # 当文本串为空时，不可能匹配成功
            return -1
        self.buildNext(needle)
        self.KMP(haystack, needle)
        return self.res

    def KMP(self, haystack, needle):
        """ KMP算法 """
        p_h, p_n = 0, 0
        while p_h < len(haystack) and p_n < len(needle):
            if haystack[p_h] == needle[p_n]:  # 文本串与模式串匹配成功，前移p_h和p_n指针
                p_h += 1
                p_n += 1
            else:  # 文本串与模式串匹配失败
                if p_n > 0:  # 如果模式串在p_n处匹配失败，p_n利用next数组回退，p_h不变
                    p_n = self.NEXT[p_n - 1]
                else:  # 如果模式串第一个字母(p_n=0)匹配失败时，p_n不变，p_h前移
                    p_h += 1
        if p_n == len(needle):  # 成功匹配完模式串
            self.res = p_h - len(needle)

    def buildNext(self, needle):
        """ 构造next数组 """
        self.NEXT = [0 for _ in range(len(needle))]  # 初始化
        front = 0
        for rear in range(1, len(needle)):
            while front > 0 and needle[rear] != needle[front]:  # 难点：匹配不成功时，回退front指针
                front = self.NEXT[front - 1]  # 不断回退front至最近一次匹配时的位置
            if needle[rear] == needle[front]:  # 匹配成功，前移front指针
                front += 1
            self.NEXT[rear] = front

