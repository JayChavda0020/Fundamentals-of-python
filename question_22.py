''' Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
If the string length is less than 2, return instead of the empty string.'''

s = input("Enter a string : ")

if len(s)>2:
    new_s = s[0:2] + s[-2:]
    print("New string is : ", new_s)
else:
    print(s)
