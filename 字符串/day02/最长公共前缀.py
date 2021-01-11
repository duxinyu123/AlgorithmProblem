class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0 :
            return ""
        min_len = len(strs[0])
        min_index = 0
        for i in range(len(strs)):
            if len(strs[i]) < min_len:
                min_len = len(strs[i])
                min_index = i
        i, j = 0, 1
        while j <= min_len:
            while i < len(strs):
                if strs[min_index][0:j] != strs[i][0:j]:
                    return strs[min_index][0:j-1]
                else:
                    i += 1
            i = 0
            j += 1
        return strs[min_index]

if __name__ == '__main__':
    # s = Solution()
    # print(s.longestCommonPrefix(["flower","flow","flight"]))
    a = ["flower", "flow", "flight"]
    a.sort()
    print(a)