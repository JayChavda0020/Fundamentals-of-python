# Write a Python program to count the occurrences of each word in a given sentence

s = input("Enter a sentence : ")
d = dict()

s = s.lower()
word = s.split(" ")

for i in word:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)



