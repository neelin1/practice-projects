class Solution:

    @staticmethod
    def compareChars(i, strs, iStr):
        for s in strs:
            if i >= len(s) or s[i] != iStr[i]:
                return False
        return True

    def longestCommonPrefix(self, strs: list[str]) -> str:
        pre = ""
        if len(strs) == 0:
            return pre
        iStr = strs[0]
        if len(strs) == 1:
            return iStr
        for i in range(len(iStr)):
            if self.compareChars(i, strs, iStr):
                pre = pre + iStr[i]
            else:
                break
        return pre
