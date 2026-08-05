import sympy as sp

# Define the symbolic variable x
x = sp.Symbol('x')


print("Trigonometric Operations:")
print("1.sin")
print("2.cos")
print("3.tan")
print("4.cot")
print("5.sec")
print("6.csc")


choice = int(input("Enter the number of the operation you want to differentiate (1-6): "))


if choice == 1:
    function = sp.sin(x)
    derivative = sp.diff(function, x)
    print(f"Function: sin(x)")
    print(f"Derivative: {derivative}")
elif choice == 2:
    function = sp.cos(x)
    derivative = sp.diff(function, x)
    print(f"Function: cos(x)")
    print(f"Derivative: {derivative}")
elif choice == 3:
    function = sp.tan(x)
    derivative = sp.diff(function, x)
    print(f"Function: tan(x)")
    print(f"Derivative: {derivative}")
elif choice == 4:
    function = 1 / sp.tan(x)  # cotangent
    derivative = sp.diff(function, x)
    print(f"Function: cot(x)")
    print(f"Derivative: {derivative}")
elif choice == 5:
    function = 1 / sp.cos(x)  # secant
    derivative = sp.diff(function, x)
    print(f"Function: sec(x)")
    print(f"Derivative: {derivative}")
elif choice == 6:
    function = 1 / sp.sin(x)  # cosecant
    derivative = sp.diff(function, x)
    print(f"Function: csc(x)")
    print(f"Derivative: {derivative}")
else:
    print("Invalid choice. Please select a number between 1 and 6.")
