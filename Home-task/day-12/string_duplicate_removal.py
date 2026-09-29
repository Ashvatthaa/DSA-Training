#to remove duplicate characters from a string
class Solution:
    def removeDuplicates(self, s):
        freq = [0] * 128
        ans = ""

        for ch in s:
            if freq[ord(ch)] == 0:
                ans += ch
                freq[ord(ch)] = 1

        return ans