class Solution:
    def __init__(self):
        self.NEXT = []
        self.res = -1

    def strStr(self, haystack: str, needle: str) -> int:
        len_h, len_n = len(haystack), len(needle)
        if len_n == 0:
            return 0
        if len_n > len_h:
            return -1
        self.build_next(needle)
        i = 0
        j = 0
        while i < len_h and j < len_n:
            if haystack[i] == needle[j]:
                i+=1
                j+=1
            else:
                if j > 0:
                    j = self.NEXT[j-1]
                else:
                    i += 1
        if j == len_n:
            return i-len_n
        else:
            return -1
        # while i <= len_h - len_n:
        #     flag = False
        #     for j in range(len_n):
        #         if haystack[i+j] == needle[j]:
        #             if j == len_n - 1:
        #                 self.res = i
        #                 return self.res
        #             continue
        #         else:
        #             if j > 0:
        #                 j = self.NEXT[j-1]
        #             else:
        #                 i = i+1
        #             break

        return self.res

    '''
    求子串的next数组，即最长相等前后缀子串的长度
    例如:
    bcbcb字符串从前到后可以拆分成以下子串：
    b: 无前后缀，所以next[0] = 0
    bc: 前缀 b 后缀 c , next[1] = 0
    bcb: 前缀 b bc 后缀 cb b , next[2] = 1
    bcbc: 前缀 b bc bcb 后缀 cbc bc c, next[3] = 2
    bcbcb: 前缀 b bc bcb bcbc 后缀 cbcb bcb cb b, next[4] = 3
    即 next = [0,0,1,2,3]
    '''
    def build_next(self, needle):
        self.NEXT = []
        for i in range(len(needle)+1):
            if i == 0:
                continue
            max_len = 0
            str = needle[0:i]
            for j in range(i):
                if j <= 0:
                    continue
                if str[0:j] == str[i-j:i]:
                    max_len = len(str[0:j])
            self.NEXT.append(max_len)
        print(self.NEXT)


s = Solution()
# print(s.strStr('abcabfdgeabcabe', 'abcabe'))
# print(s.strStr('hello', 'll'))
# print(s.strStr('mississippi', 'issi'))
print(s.strStr('babbbbbabb', 'bbab'))

# s.build_next('abcab')