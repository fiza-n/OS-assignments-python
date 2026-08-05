import sympy as sp

def compute_derivative(expression, variable):
   
    x = sp.symbols(variable)
    
   
    expr = sp.sympify(expression)
    
   
    derivative = sp.diff(expr, x)
    
    return derivative

def main():
    
    expression = input("Enter a mathematical expression (e.g., x**2 + 3*x + 5): ")
    variable = input("Enter the variable with respect to which the derivative should be calculated (e.g., x): ")
    
    result = compute_derivative(expression, variable)
    
    print(f"The derivative of {expression} with respect to {variable} is: {result}")

if __name__ == "__main__":
    main()
