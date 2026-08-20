# my_list = [0,1,2,3,4,5,6,7,8,9]
# #          0,1,2,3,4,5,6,7,8,9
# #        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# # list[start:end:step]

# print (my_list[3:8:3])
# print (my_list[::-10]) #reverse


# # strings

# url = "http://coreys.com"
# # reverse
# print(url[::-1])

# # print only .com
# print(url[-4:])

# # only http://
# print(url[7:])

# print(url[7:-4])

# list comprehensions
# nums = [1,2,3,4,5,6,7,8,9]
# my_list = []
# # for n in nums:
# #     my_list.append(n)
# # similar
# my_list = [n for n in nums]

# print(my_list)

# nums = [1,2,3,4,5,6,7,8,9]
# # my_list = []
# # for n in nums:
# #     my_list.append(n*n)
# # similar
# my_list = [n*n for n in nums]

# print(my_list)

# nums = [1,2,3,4,5,6,7,8,9]
# my_list = []
# # for n in nums:
# #     if n%2 == 0:
# #         my_list.append(n)
# # similar
# my_list = [n for n in nums if n%2 ==0]

# # using filter + lambda
# my_list = list(filter(lambda n: n%2 == 0 , nums))

# print(my_list)

# string list comprehension
# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter, num))

# similar to
# my_list = [(letter, num) for letter in 'abcd' for num in range(4)]

# print(my_list)

# comprehension for dict

# names = ["bruce", "tony", "steve", "clint", "nat"]
# heroes = ["hulk", "ironman", "captain america", "clint", "black widow"]

# print(list(zip(names, heroes)))

# my_dict = {}

# # for name, hero in zip(names,heroes):
# #     my_dict[name] = hero

# # similar to
# my_dict = {name: hero for name, hero in zip(names, heroes)}

# print(my_dict)


# comprehension for set

nums = [1,2,3,4,5,6,7,8,9]
my_set = set()

# for n in nums:
#     my_set.add(n)

# similar
my_set = {n for n in nums}
print(my_set)

words = ["apple", "kiwi", "banana", "fig", "mango"]

words = [w.upper() for w in words if len(w) > 3]

print(words)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix = [n for row in matrix for n in  row if n%2 == 0]

print(matrix)
print([n for n in range(100) if n%3 == 0 and n%5 == 0])
