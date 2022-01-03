#1 create file and text what is your goals for this year.

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
#2 creat a lambda function using arguments
a = lambda x,y,z: x*y+z
print(a(1,2,3))

print ("-------------------------------------------------------")
#3 Create a function that uses the user input. 

def add(x):
    return "Happy new year " + x


print(add(input("what is your name: ")))

print ("-------------------------------------------------------")
#4 Create a whileloop that prints 1-30 but skips 25.

x = 0
num = []
while x < 30:
    x+=1
    if x != 25:
        num.append(x)
    
print(num)
print ("-------------------------------------------------------")

#5 Create a function that prints out random numbers. Use 2 arguments. 

import random

def guess(a,b):

    return "random number between " + str(a)+" and " + str(b) + " is " + str(random.randint(a, b))

z = guess(int(input("Enter 1st number")), int(input ("Enter 2nd number")))


print (z)














