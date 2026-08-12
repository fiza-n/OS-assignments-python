x = 'Pluto is a planet'
y = "Pluto is a planet"
x == y

print('Pluto\'s planet')
print("Pluto's planet")
print('Pluto is "planet"')

hello = "hello\nworld"
print(hello)

triplequoted_hello = """hello world"""
print(triplequoted_hello)
triplequoted_hello == hello

print("hello")
print("world")
print("hello", end='\'')
print("pluto")

# Indexing SEQUENCE
planet = 'Pluto'
print(planet[0])
# Slicing
print(planet[-1:])

# How long is this string?
print(len(planet))
result = [char+'! ' for char in planet]
print(result)

# #cannot modify
# planet[0] = 'B'
# # planet.append doesn't work either

# ALL CAPS
claim = "Pluto is a planet!"
print(claim.upper())

# all lowercase
claim.lower()
# Searching for the first index of a substring
print(claim.index('plan'))

claim.startswith(planet)
# false because of missing exclamation mark
claim.endswith('planet')

#str.split() turns a string into a list of smaller strings, breaking on whitespace by default
words = claim.split()
print(words)

datestr = '1956-01-31'
year, month, day = datestr.split('-')
print(year,month, day)

#opposite of split
print('/'.join([month, day, year]))
# planet = ' 👏 '.join([word.upper() for word in words])
print(planet)
print(planet + ', we miss you.')
position = 9
print(planet + ", you'll always be the " + str(position) + "th planet to me.")

print("{}, you'll always be the {}th planet to me.".format(planet, position))

name = 'Fiza'
age = 21

print("I'm {}, and my age is {}".format(name,age))#Notice how we didn't even have to call str()

# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)