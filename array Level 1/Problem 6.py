'''
Find the frequency of a number in an array
'''
def frequency(a, x):
    count = 0

    for i in a:
        if i == x: count += 1
    return count


# Driver program
a = [0, 5, 5, 5, 4]
x = 5
print(frequency(a, x))

# This code is contributed by Ansu Kumari
