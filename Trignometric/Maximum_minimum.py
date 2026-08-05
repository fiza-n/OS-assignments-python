



from sympy import symbols, diff, solve, sympify


variable = input("Enter the variable (e.g., x): ")
expression = input("Enter the function (e.g., x*3 - 3*x*2 + 4): ")

var = symbols(variable)
func = sympify(expression)

first_derivative = diff(func, var)

critical_points = solve(first_derivative, var)


second_derivative = diff(first_derivative, var)


results = []
for point in critical_points:
    second_derivative_value = second_derivative.subs(var, point)
    if second_derivative_value > 0:
        results.append((point, "Minimum"))
    elif second_derivative_value < 0:
        results.append((point, "Maximum"))
    else:
        results.append((point, "Point of Inflection"))

print("The critical points and their classification are:")
for point, classification in results:
    print(f"At x = {point}, the function has a {classification}.")
