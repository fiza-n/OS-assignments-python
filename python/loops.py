nums = [1,2,3,4,5]

# # for loop
# for num in nums:
#     if(num == 2):
#         break
#     print(num)

# loop in a loop
# for num in nums:
#     for letter in 'abc':
#         print(num, letter)

# for i in range(10):
#     print(i)

# def dup_len(some_string):
#     return some_string.count(some_string)

# print(dup_len('test'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
    
courses= ['Math', 'Arts']
info={'name': 'fiza', 'age': 22}

student_info(*courses, **info)