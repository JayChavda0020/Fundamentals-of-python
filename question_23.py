# Write a Python function to insert a string in the middle of a string

s = input("Enter a string : ")

mid_str = input("Enter middle string : ")

s1 = s.split()

print("*"*50)

print("The original string is : ", str(s))

mid = len(s1) // 2 

final_str = s1[:mid] + [mid_str] + s1[mid:]

final_str = ' '.join(final_str)

print("*"*50)

print("New string is : ", final_str)