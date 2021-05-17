def search(list, n):

    l = 0
    u = len(list)-1
    mid = 0
    while l <= u :
        mid = (l+u )  // 2
        if list[mid] > n:
            u = mid - 1
        elif list[mid]<n:
            l = mid + 1
        else :
            return mid

    return -1
list = [2, 3, 4, 10, 40 ]
n = 45
result = search(list , n)
if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")
