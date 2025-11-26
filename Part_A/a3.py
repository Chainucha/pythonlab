# Consider a tuple t1= (1,2,5,7,9,2,4,6,8,10). Write a program to perform following
# operations:
# a. Print half the values of tuple in one line and the other half in the next line.
# b. Print another tuple whose values are even numbers in the given tuple.
# c. Concatenate a tuple t2= (11,13,15) with t1.
# d. Return maximum and minimum value from this tuple.

t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
print("tuple is:", t1)
a = len(t1) // 2
print("First half of tuple", t1[:a])
print("second half of tuple", t1[a:])
list1 = []
for i in t1:
    if i % 2 == 0:
        list1.append(i)
t2 = tuple(list1)
print("Even number in the tuple", t2)
t2 = (11, 13, 15)
t3 = t1 + t2
print("concatenate tuple", t3)
print("maximum value:", max(t3))
print("minimum value:", min(t3))
