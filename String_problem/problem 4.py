'''
Write a Code to check whether one string is a rotation of another...
'''

def rotation(s1,s2):
    size1 = len(s1)
    size2 = len(s2)
    temp = ""

    if (size1 != size2):
        return 0

    temp = s1 + s2


    if (temp.count(s2)>0):
        return 1
    else:
        return 0

s1 = 'ABCD'
s2 = 'CDABX'

if rotation(s1,s2):
    print("The Given String is Rotationals")
else:
    print("The Given String is not Rotationals")


