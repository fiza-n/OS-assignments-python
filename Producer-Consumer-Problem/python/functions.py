from functools import singledispatch
# help(round)

def least_difference(a,b,c):
    """Return the minimum absolute difference among three values."""
    diff1 = abs(a-b)
    diff2 = abs(b-c)
    diff3 = abs(a-c)

    return min(diff1, diff2, diff3)

print(least_difference(2,4,7))
print("\nDocstring:")
print(least_difference.__doc__)
print(round.__doc__)
print(round(3.5), round(3.14159, 2))

#ways to define a function with same name
def least_difference(a, b, c):#overwriting the previous function
    """Return the smallest difference between any two numbers
    among a, b and c.
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    min(diff1, diff2, diff3)
    
print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),
)
print(least_difference(2,3,4))

def total_sum(*numbers):# variable arguments
    return sum(numbers)

print(total_sum(1, 2))       # Returns 3
print(total_sum(1, 2, 3, 4)) # Returns 10


@singledispatch
def process(data):
    raise NotImplementedError("Unsupported type")

@process.register(int)
def _(data):
    return f"Processing integer: {data}"

@process.register(str)
def _(data):
    return f"Processing string: {data.upper()}"

print(process(10))     # Returns: Processing integer: 10
print(process("test")) # Returns: Processing string: TEST
#print(process(3.4)) #NotImplementedError: Unsupported type

#Adding optional arguments with default values to the functions we define turns out to be pretty easy:

def greet(who="Colin"):
    print("Hello,", who)
    
greet()
greet(who="Kaggle")
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("world")


# You can supply functions as arguments to other functions.
#higher-order-function
def mult_by_five(x):
    return x * 5

def call(fn, val):
    return fn(val)

def sqaure(fn,val):
    return fn(fn(val))

print(
    call(mult_by_five, 3),
    sqaure(mult_by_five, 3),
    sep=" , "
)

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),#return largest output's input
    sep='\n',
) 
print(x , 4)

