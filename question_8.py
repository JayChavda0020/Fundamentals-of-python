# Write a Python program to test whether a passed letter is a vowel or not

letter = (input("Enter a letter : "))

vowel = ['a','e','i','o','u','A','E','I','O','U']

if letter in vowel:
    print(letter, "is vowl")
else:
    print(letter, "is not vowl")