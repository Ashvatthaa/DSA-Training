#Give the input string and print the index of each character in the string along with the character itself.

string = input("Enter a string: ")
for i in string:
    print(string.index(i),":", i)