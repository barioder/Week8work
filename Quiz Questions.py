# 2
a = 25
b = 30

print(f"{a}{b}")

names1 = ['Amir', 'Barry', 'Chales', 'Dao']

loc = names1.index("Barry")
print(loc)
print("------------------")

x = 13%15
print(x)

print("------------------")
word = "HOW ARE YOU"
print(word.count('A'))

z = 23.0*4
print(z)

y =("Dave", "Jamie", "Jill", "Brenda")

print(y[1])

print(y[-4])

print(y[3:])
#
# cat_weight = 45
# if cat_wieght = 50;
# print your cat is healthy
#
# else: print unhealthy

l = (1, 2, 3)

print(l[2])

a_list = [10, 20, 30, 40]

print(a_list[-1])
print("------------------")

import random

print(random.randint(1,6))

print(20 + 10 ** 2)


class Animal:
    def __init__(self, name, age, pet_owner):
        self.name = name
        self.age = age
        self.pet_owner = pet_owner


class Cat(Animal):
    def pet(self):
        print("The Cat " + self.name + " of age " + self.age + " is owned by " + self.pet_owner)


owner1 = Cat("Gafi", "1", "Derrick")

owner1.pet()
#
# print('3\')
"He said','Yes!'"
# ""'Once upon time....",She said.'
# print("'That's Okay""')

grade1 = 80

grade2 = 90

average = (grade1 + grade2) / 2

print(average)

a = 3^4
print(a)


print(3*1**3)

def lessThan(a):
    list = []
    i = 0
    while i < a:
        i += 1
        if i%2 == 0 and i%6 == 0:
            list.append(i)

    return print (list)

lessThan(25)

#Create a program that prints out odd numbers using the while loop.

print("------------------")
x = 0
while x < 6:

    if x%2 == 1:
        print(x)

    x += 1


print("------------------")

c = [x for x in range(1,10) if x%2 == 1]

print(c)