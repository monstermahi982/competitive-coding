def reverseList(A):
    print(A[::-1])



# Driver function to test above function
A = ["a","s","f","j","i"]
print(A)
print("Reversed list is")
reverseList(A)

#___________________________________________________
'''
def reverse(a ,start , last):
    while start < last:
        a[start],a[last] = a[last],a[start]
        start+=1
        last-=1

a= [1,2,4,5,6,7]
reverse(a,0,5)
print(a)
'''