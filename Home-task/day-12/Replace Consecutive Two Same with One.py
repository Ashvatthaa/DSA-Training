# replace consecutive two same characters with one:https://www.geeksforgeeks.org/problems/consecutive-elements2306/1
class Solution:
    def removeDuplicates(self, s):
        ans = [s[0]]

        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                ans.append(s[i])

        return "".join(ans)