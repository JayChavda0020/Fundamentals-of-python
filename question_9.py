'''Write a Python program to sum of three given integers. However, if
two values are equal sum will be zero.'''

x = int(input("Enter number X : "))
y = int(input("Enter number Y : "))
z = int(input("Enter number Z : "))

if x==y:
    print("Sum is zero")
elif y==z:
    print("Sum is zero")
elif x==z:
    print("Sum is zero")
else:
    print("Sum of x,y,z is", x+y+z)