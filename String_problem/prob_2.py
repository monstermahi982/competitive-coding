'''
Check whether a String is Palindrome or not
'''
''' 
#Using iterating Element
#stri =""

def rev(l):
    stri = ""
    for i in l:
        stri = i + stri
    if  (stri == l):
        print("The string {} is a Palindrome".format(l))
    else:
        print("The string {} is not a Palindrome".format(l))
    return stri

l = "POO"
print(rev(l))
'''
# Using Slicing
'''
str ="Psss"
s = str[::-1]
print(s)
if(s==str):
    print("The string {} is a Palindrome".format(str))
else:
    print("The string {} is not a Palindrome".format(str))
    
'''