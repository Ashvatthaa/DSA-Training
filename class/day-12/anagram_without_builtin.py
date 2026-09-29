s1 = input()
s2 = input()

if len(s1) != len(s2):
    print("Not Anagram")
else:
    count = [0] * 26

    for ch in s1:
        count[ord(ch) - ord('a')] += 1

    for ch in s2:
        count[ord(ch) - ord('a')] -= 1

    is_anagram = True
    for i in range(26):
        if count[i] != 0:
            is_anagram = False
            break

    if is_anagram:
        print("Anagram")
    else:
        print("Not Anagram")


# Another approach to check if two strings are anagrams without using built-in functions is to use a dictionary to count the occurrences of each character in both strings and then compare the counts with time complexity O(n) and space complexity O(n). Here is an example implementation:

#class Solution:
#    def areAnagrams(self, s1, s2):
#        if len(s1) != len(s2):
#            return False
#        seen = {} 
#        for i in s1:
#            if i in seen:
#                seen[i] += 1
#            else:
#                seen[i] = 1
#        for j in s2:
#            if j not in seen:
#                return False
#            seen[j] -= 1
#        return all(value == 0 for value in seen.values())