'''
Find the frequency of a number in an array
Difficulty Level : Easy
Last Updated : 24 Feb, 2020
Given an array a[] and an element x, find number of occurrences of x in a[].

Examples:

Input  : a[] = {0, 5, 5, 5, 4}
           x = 5
Output : 3

Input  : a[] = {1, 2, 3}
          x = 4
Output : 0
'''
a = []
size = int(input("Enter the Size of list"))
for i in range(size):
    val = int(input("Enter the number"))
    a.append(val)

key = int(input("Enter the x value"))
count = 0
for i in range(size):
    if(a[i]==key):
        count+=1

print("frequency :",count)