'''Move all negative numbers to beginning and positive to end with constant extra space
Difficulty Level : Easy
Last Updated : 22 Dec, 2020
An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.
Examples : 

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5
'''
def reaarange(arr , n):
    j = 0
    for i in range(0 , n):
        if arr[i]< 0:
            temp  = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j +=1

    print(arr)
arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
n = len(arr)
reaarange(arr ,n )
