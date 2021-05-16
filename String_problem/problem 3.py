"""
Find Duplicate characters in a string

"""
str = "pop"
for i in range(0,len(str)):
    count = 1
    for j in range(i+1,len(str)):
        if(str[i]==str[j] and str[i]!=" "):
            count = count+1
            str = str[:j]+'0'+ str[j+1:];
    if(count>1 and str[i]!='0'):
        print(str[i])

str = "Suved Chougule"

for i in range(0,len(str)):
    countt = 1
    for j in range(i+1,len(str)):
        if(str[i]==str[j] and str[i]!=" "):
            countt = countt +1
            str = str[:j] + '0' + str[j+1:];
    if(countt>1 and str[i]!='0'):
        print(str[i])

