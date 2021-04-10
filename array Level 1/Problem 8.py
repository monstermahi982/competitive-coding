'''
Range and Coefficient of range of Array
Difficulty Level : Basic
Last Updated : 17 Dec, 2018
Given an array arr of integer elements, the task is to find the range and coefficient of range of the given array where:
Range: Difference between the maximum value and the minimum value in the distribution.
Coefficient of Range: (Max – Min) / (Max + Min).

Examples:

Input: arr[] = {15, 16, 10, 9, 6, 7, 17}
Output: Range : 11
Coefficient of Range : 0.478261
Max = 17, Min = 6
Range = Max – Min = 17 – 6 = 11
Coefficient of Range = (Max – Min) / (Max + Min) = 11 / 23 = 0.478261

Input: arr[] = {5, 10, 15}
Output: Range : 10
Coefficient of Range : 0.5

'''
def gmin(arr, n):
    res = arr[0]
    for i in range(1,n,1):
        res = min(res,arr[i])
    return res

def gmax(arr, n):
    res = arr[0]
    for i in  range(1,n,1):
        res = max(res,arr[i])
    return res
def getcoe(arr , n):
    min = gmin(arr, n)
    max = gmax(arr,n)
    rng = max-min
    coe = rng / (max+min)
    print("Range :: " , rng)
    print("Coefficient of Range : " , coe)


if __name__ == "__main__":
    arr = [10,15,20]
    n = len(arr)
    getcoe(arr,n)