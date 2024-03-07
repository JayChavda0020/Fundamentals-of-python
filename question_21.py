# Write a Python function to reverses a string if its length is a multiple of 4.

s = input("Enter a string : ")
l = len(s)

if l%4 == 0:
    print(s[::-1])
else:
    print(s)


