
# #lists (are mutable can be changed)
# # names = ["fiza", "iqra", "mehak"]
# # print(names[0])

# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# print(planets[-1]) #accessing the last element 
# print(planets[0:3])#slicing
# print(planets[:-1])
# print(planets[-3:])
# #modifiable
# planets[3] = 'Malacandra'
# planets[:3] =  ['Mur', 'Vee', 'Ur']
# print(planets)

# #list functions
# print(len(planets))

# # The planets sorted in alphabetical order
# print(sorted(planets))

# #sum of list
# primes = [2, 3, 5,[2,3]]
# print(len(primes))
# # print(sum(primes[0]))

# #max of list
# # print(max(primes[0]))

# #objects in list
# x = 12
# print(x.imag)
# c = 12 + 3j
# real = int(c.real)
# print(help(real.bit_length()))

# #list methods
# #list.append modifies a list by adding an item to the end:

# planets.append('Pluto')
# print(planets)

# #list.pop removes and returns the last element of a list:
# print(planets.pop())
# print(planets)

# print(planets.index('Ur'))
# print("pluto" in planets)
# d = [1, 2, 3][1:]
# print(len(d))
# print("Index:", planets.index('Ur'))

# courses.replace('History','CompSci')
# courses.insert(0,'CompSci') we can also insert a whole list

# courses_2 = ['OS', 'DSA']
# courses.extend(courses_2)
# courses.remove('English')
# courses.reverse()
# courses.sort()
# popped = courses.pop()
# print(popped)
# print(courses)

nums = [1,4,5,3,2]
sorted_nums = sorted(nums)
# nums.sort(reverse=True) #descending order
print(sorted_nums)

print(min(nums))
print(max(nums))

courses = ['History', 'Physics', 'English', 22]
list()
# loop in list

for index, course in enumerate(courses, start=1):
    print(index,course)

#tuples
information = ("Fiza", 22, courses)
tuple()

print(information)

# sets (unordered and not allow duplicates)
set()
cs_courses = {'History', 'Physics', 'Math', 'CompSci'}
art_courses = {'History', 'Physics', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))
