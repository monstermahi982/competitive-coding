"""
Reverse a String
"""
# using Slicing

s = "Hello" [::-1]
print(s)
'''
# Loop Using

'''
''''
def rev(s):
    str= ""
    for i in s:
        str = i + str
    return str
s = "Geetagovindam"

print(rev(s))
'''
'''
# Using Reversed Function

# Python code to reverse a string
# using reversed()

# Function to reverse a string
def reverse(str):
	str = "".join(reversed(str))
	return str

s = "Govinda"
print ("The reversed string(using reversed) is : ")
print (reverse(s))
'''