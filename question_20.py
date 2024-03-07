# Write a Python function that takes a list of words and returns the length of the longest one.

def longestLength(a):
    max = len(a[0])
    temp = a[0]

    for i in a:
        if len(i) > max:
            max = len(i)
            temp = i 

    print("The longest word is : ", temp, "and length is : ", max)

a = ["one","two","four","five"]
longestLength(a)