from sympy import symbols, diff

x = symbols('x')


user_input = input("Enter the function in terms of x (e.g., x**3 + 2*x**2 - 5*x + 7): ")


function = eval(user_input)

first_derivative = diff(function, x)


second_derivative = diff(first_derivative, x)

print(f"Function: {function}")
print(f"First Derivative: {first_derivative}")
print(f"Second Derivative: {second_derivative}")
