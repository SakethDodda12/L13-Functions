def add(P, Q):
    return P+Q
def sub(P, Q):
    return P-Q
def mult(P, Q):
    return P*Q
def div(P,Q):
    return P/Q

print("Select the operation needed to be done:")
print("A. Add")
print("B. Subtract")
print("C. Multiply")
print("D. Divide")

choice = input("Please enter a letter from th list: ")
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if choice == 'a':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == 'b':
    print(num1, "-", num2, "=", sub(num1, num2))
elif choice == 'c':
    print(num1, "*", num2, "=", mult(num1, num2))
elif choice == 'd':
    print(num1, "/", num2, "=", div(num1, num2))