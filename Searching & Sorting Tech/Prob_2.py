'''Input: arr[] = {-10, -5, 0, 3, 7}
  Output: 3  // arr[3] == 3 

  Input: arr[] = {0, 2, 5, 8, 17}
  Output: 0  // arr[0] == 0 


  Input: arr[] = {-10, -5, 3, 4, 7, 9}
  Output: -1  // No Fixed Point
'''
list = [-10, -5, 0, 3, 7]
a = 0
for i in range(0,len(list)):
    if list[i]==i:
        a = i
print("Fixed Point is {}".format(a))
