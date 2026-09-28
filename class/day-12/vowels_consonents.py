#Count the number of vowels and consonents in the given string.The string will contain both upper case and lower case letters.
string=input()
vowel=0
consonent=0
for i in string:
    if i in "aeiouAEIOU":
        vowel+=1
    else:
        consonent+=1
print(f"Vowels:{vowel}\nConsonents:{consonent}")