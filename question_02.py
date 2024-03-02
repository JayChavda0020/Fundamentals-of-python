# Write a Python program to get the Factorial number of given number.

n = int(input("Enter a number : "))

factorial = 1

if n>0:
    for i in range(1,n+1):
        factorial = factorial * i
    print("Factorial is : ", factorial)

elif n<0:
    print("Factorial does not exist for negative number")

else:
    print("Factorial of 0 is 1")