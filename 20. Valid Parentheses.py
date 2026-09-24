class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        store = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for i in s:
            if i in "{[(":
                store.append(i)
            else:
                if not store or store[-1] != pairs[i]:
                    return False
                else:
                    store.pop()
        if store:
            return False
        return True
        


solution = Solution()

print(solution.isValid("(]"))