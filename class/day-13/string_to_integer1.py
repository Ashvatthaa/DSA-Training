s = input("Enter the string:")   
parts = s.split()
a = int(parts[0])
op = parts[1]
b = int(parts[2])
if op == "+":
    print("sum =", a + b)
elif op == "-":
    print("difference =", a - b)
elif op == "*":
    print("product =", a * b)
elif op == "/":
    print("quotient =", a / b)
elif op == "//":
    print("floor division =", a // b)
elif op == "%":
    print("remainder =", a % b)
else:
    print("Invalid")