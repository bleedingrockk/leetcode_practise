class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common = strs[0]
        for i in strs:
            while not i.startswith(common):
                common = common[:-1]

                if common == "":
                    return ""
        return common

    
solution = Solution()
list1 = ["flower","flow","flight"]
print(solution.longestCommonPrefix(list1))
