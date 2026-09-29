s = input()      # Example: 256 + 72

num1 = 0
num2 = 0
op = ''
i = 0

# First number
while s[i] != ' ':
    num1 = num1 * 10 + (ord(s[i]) - ord('0'))
    i += 1

i += 1          # Skip space
op = s[i]       # Operator
i += 2          # Skip operator and space

# Second number
while i < len(s):
    num2 = num2 * 10 + (ord(s[i]) - ord('0'))
    i += 1

# Perform operation
if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)
elif op == '%':
    print(num1 % num2)