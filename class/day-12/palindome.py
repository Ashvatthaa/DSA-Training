#Chceck if the given string is palindrome or not using slicing with time complexity O(n) and space complexity O(n).
s = input()

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# This is another way to check for palindrome using two pointers approach with time complexity O(n) and space complexity O(1).

#s = input()
#left = 0
#right = len(s) - 1
#
#while left < right:
#    if s[left] != s[right]:
#        print("Not Palindrome")
#        break
#    left += 1
#    right -= 1
#else:
#    print("Palindrome")