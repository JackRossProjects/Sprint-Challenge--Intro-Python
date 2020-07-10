# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = []
for i in humans:
    if i.name[0] == 'D':
        a.append(i.name)
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []
for i in humans:
    if i.name[-1] == 'e':
        b.append(i.name)
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = []
cToG = ['C', 'D', 'E', 'F', 'G']
for i in humans:
    if i.name[0] in cToG:
        c.append(i.name) 
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = []
for i in humans:
    i.age += 10
    d.append(i.age)
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []
for i in humans:
    name = i.name
    age = i.age
    e.append(str(i.name) + "-" + str(i.age))
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []
for i in humans:
    if i.age > 26 and i.age < 33:
        f.append((i.name, i.age,))
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = []
for i in humans:
    g.append(Human(i.name.upper(), i.age + 5))
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = []
for i in humans:
    h.append(math.sqrt(i.age))
print(h)


'''
Some of the tests fail but I'm not sure why. Seems to me that all of them are solved except f.

Terminal output:

Starts with D:
['Daphne', 'David']
Ends with e:
['Alice', 'Charlie', 'Daphne', 'Eve']
Starts between C and G, inclusive:
['Charlie', 'Daphne', 'Eve', 'Frank', 'Glenn', 'David']
Ages plus 10:
[39, 42, 47, 40, 36, 28, 52, 22, 51, 41]
Name hyphen age:
['Alice-39', 'Bob-42', 'Charlie-47', 'Daphne-40', 'Eve-36', 'Frank-28', 'Glenn-52', 'Harrison-22', 'Igon-51', 'David-41']
Names and ages between 27 and 32:
[('Frank', 28)]
All names uppercase:
[<Human: ALICE, 44>, <Human: BOB, 47>, <Human: CHARLIE, 52>, <Human: DAPHNE, 45>, <Human: EVE, 41>, <Human: FRANK, 33>, <Human: GLENN, 57>, <Human: HARRISON, 27>, <Human: IGON, 56>, <Human: DAVID, 46>]
Square root of ages:
[6.244997998398398, 6.48074069840786, 6.855654600401044, 6.324555320336759, 6.0, 5.291502622129181, 7.211102550927978, 4.69041575982343, 7.14142842854285, 6.4031242374328485]
.F..FFF.
'''