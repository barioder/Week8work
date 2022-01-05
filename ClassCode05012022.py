# 1.Write a program to take a number as input, and output a list of all
#the numbers below that number, that are a multiple of both, 3 and 5.
def lower(a):
    list = []
    i = 0
    while i < a:
        i += 1
        if i%3 == 0 and i%5 == 0:
            list.append(i)

    return print (list)

lower(250)
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')



# 2. Create a nesting list.
people = [['tim ',45], ['derrick ', 35]]
t = 0
for name,age in people:
    print( name + str(age))
        
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')




#3. Using the list comprenhension, print only odd numbers.

result = [x for x in range(1,15,1) if x%2 == 1]

print(result)

print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')




#4. Create a 4-D list and grab two elements out of that list.
h = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
a = h[2:]
print(a)
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')



#5. Create a program that merge 2 list together.

list1 = [1, 2 , 3 ]
list2 = [4, 5, 6]

for item in list2:
    list1.append(item)

print(list1)
