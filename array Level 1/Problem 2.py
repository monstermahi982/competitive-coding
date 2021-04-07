'''Program to find the minimum (or maximum) element of an array'''

#def getMin(arr , n):
 #   return min(arr)


#def getMax(arr , n):
#    return max(arr)



#if __name__ == '__main__':
 #   arr = [23,56,78,96,4,34,55,32]
  #  n = len(arr)

   # print("Minimum Element of Array : ",getMin(arr,n))
    #print("Maximum Element of Array : ",getMax(arr , n))

#_________________________________________________________________________
'''
def getmin(arr ,n):
    if (n==1):
        return arr[0]
    else:
        min(getmin(arr[1:],n-1),arr[0])

def getmax(arr , n):
    if (n==1):
        return arr[0]
    else:
        max(getmax(arr[1:], n-1), arr[0])

arr = [23,56,78,96,4,34,55,32]
n = len(arr)
print("Minimum Element of Array : ", getmin(arr, n))
print("Maximum Element of Array : ",getmax(arr , n))
'''
#________________________________________________________________
'''
arr = [23,56,78,96,4,34,55,3]
print(max(arr))
print(min(arr))
'''