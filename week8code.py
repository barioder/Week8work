# 1 create file and text what is your goals for this year.

import os
# f = open("new year.txt", "x")
# f.close()

f = open("new year.txt", "w")
f.write("What is your goals for this year.\n")
f.write("\t1.Chase bigger goals\n")
f.write("\t2.Get the required certifictes")
f = open("new year.txt", "r")

print(f.read())
f.close()

print ("-------------------------------------------------------")
# 2 creat a lambda function using arguments
a = lambda x,y,z: x*y+z
print(a(1,2,3))

print("-------------------------------------------------------")
# 3 Create a function that uses the user input.


def add(x):
    return "Happy new year " + x


print(add(input("what is your name: ")))

print("-------------------------------------------------------")
# 4 Create a whileloop that prints 1-30 but skips 25.

x = 0
num = []
while x < 30:
    x+=1
    if x != 25:
        num.append(x)
    
print(num)
print("-------------------------------------------------------")

# 5 Create a function that prints out random numbers. Use 2 arguments.


import random


def guess(a, b):

    return "random number between " + str(a)+" and " + str(b) + " is " + str(random.randint(a, b))


z = guess(int(input("Enter 1st number")), int(input ("Enter 2nd number")))


print(z)

# Tuesday 4th Jan 2022

# 1.Write a function that takes a string and a letter as its arguments
# and returns the count of the letter in string.Hint use the user input and the count method.

# string = input('Write some random text: ')
# letter = input('In put any random letter: ')

#
# def count(string, letter):
#     return string.count(letter)
#
#
# print(count(input('Write some random text: '), input('In put any random letter: ')))
#
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
# 2. Create a list that prints all items in your list from uppercase to lowercase.

names = ['ALEX', 'TIM', 'DERRICK']

for name in names:
    print(name.lower())


print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

# 3. Create a while loop that prints odd numbers from 1 - 15 but skips 5.
a = []
b = []
z = 0

while z < 16:
    z += 1
    if z != 5:
        if z % 2 == 1:
            a.append(z)
    else:
        continue

print(f"list a = {a}")

# Doing the same thing using a for loop

for i in range(1, 16, 2):
    if i != 5:
        b.append(i)

print(f"list b = {b}")


print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')


# 4. Create a tuple of items and convert it into a list.

a = (1, 3, 5, 7)
c = list(a)
print(c)


# lists

list = [['John', 24], ['Brenda', 40]]

for name, age in list:
    print(name + ":", age)

# list comprehension
names = ["John", 'Brenda']
ages = ['32', '66']


for i in names:
    print(i)
    for j in ages:
        print(i + ':', j)

    y = [x for x in names]
    print(y)

names = ["John", 'Brenda']
z = [j for j in names if 'd' in j]

print(z)

a = [i.upper() for x in names]
print(a)

t = [i*2 for i in [1, 2, 3]]

print(t)

