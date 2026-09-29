#String to integer conversion using operator module
import operator
a = input("Enter the expression (e.g., '3 + 4'): ")
Input = a.split()
operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

result = operators[Input[1]](int(Input[0]), int(Input[2]))
print(result)