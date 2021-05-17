
#Using while Loop

def search(list , n):
    i = 0

    while i< len(list):
        a = 0
        if list[i] == n:
            print(i+1)
            return i
        i = i+ 1
    return -1
list = [1,5,9,7,6]
n = 5
result = search(list , n)
if result == -1:
    print("Not Found"  )
else:
    print("Found ")
'''
# Using for loop
def search(list , n):

    for i in range(len(list)):
        if list[i] == n:
            print(i+1)
            return True

list = [1,5,9,7,6]
n = 7

if search(list,n):
    print("Found")

else:
    print("Not Found")
    '''