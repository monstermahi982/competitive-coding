'''C program to sort an array in ascending order
'''
a = []
size = int(input("Enter the size of array::  "))
for i in range(size):
    val = int(input("Enter any number"))
    a.append(val)

a.sort()
print(a)