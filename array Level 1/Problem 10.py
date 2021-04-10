'''

Given two sorted arrays, find their union and intersection.
Example:

Input : arr1[] = {1, 3, 4, 5, 7}
        arr2[] = {2, 3, 5, 6}
Output : Union : {1, 2, 3, 4, 5, 6, 7}
         Intersection : {3, 5}

Input : arr1[] = {2, 5, 6}
        arr2[] = {4, 6, 8, 10}
Output : Union : {2, 4, 5, 6, 8, 10}
         Intersection : {6}
'''

def punion(arr1, arr2 , m, n):
        i,j = 0,0
        while i < m and  i < n:
            if arr1[i]<arr2[j]:
                print(arr1[i])
                i+=1
            elif arr2[j]<arr1[i]:
                print(arr2[j])
                j+=1
            else:
                print(arr2[j])
                i+=1
                j+=1

        while i<m:
            print(arr1[i])
            i+=1

        while j<n:
            print(arr2[j])
            j+=1
def pinter(arr1 , arr2 , m ,n):
    i = 0
    j = 0
    while i <m and j<n:
        if arr1[i]<arr2[j]:
            i+=1
        elif arr2[j]<arr1[i]:
            j+=1
        else:
            print(arr2[j])
            i+=1
            j+=1


arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
m = len(arr1)
n = len(arr2)
print("Union is :: ")

punion(arr1,arr2 , m , n)
print("intersection is :: ")
pinter(arr2 , arr1 , m , n)