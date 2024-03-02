# Write a Python program to count the number of characters (character frequency) in a string

s = input("Enter a string : ")

frequency = {}

for i in s:
    if i in frequency:
        frequency[i] += 1 
    else:
        frequency[i] = 1

print("Frequency of each character in given string is :\n", str(frequency))