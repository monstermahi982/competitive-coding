'''Input : arr[] = {1, 3, 5, 5, 5, 5, 67, 123, 125}
        x = 5
Output : First Occurrence = 2
         Last Occurrence = 5

Input : arr[] = {1, 3, 5, 5, 5, 5, 7, 123, 125 }
        x = 7
Output : First Occurrence = 6
         Last Occurrence = 6
'''
list = [1, 3, 5, 5, 5, 5, 67, 123, 125]
x = 5
first = -1
last = -1
for i in range(0,len((list))):
    if x != list[i]:
        continue


    if first == -1:
        first = i
    last = i

if first != -1:
    print("First Occurence is ", first)
    print("Last Occurence is",last)
else:
    print("Not Found")

