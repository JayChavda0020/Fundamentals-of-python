# Write python program that swap two number with temp variable and without temp variable.

a = int(input("Enter number A : "))
b = int(input("Enter number B : "))

print("Value of A before swapping : ", a)
print("Value of B before swapping : ", b)

temp = a
a = b
b = temp

print("*"*50)
print("Value of A after swapping : ", a)
print("Value of B after swapping : ", b)

# without temp variable.

print("*"*50)
c = int(input("Enter number C : "))
d = int(input("Enter number D : "))

print("*"*50)
print("Value of C before swapping : ", c)
print("Value of D before swapping : ", d)

c,d = d,c

print("*"*50)
print("Value of C after swapping : ", c)
print("Value of D after swapping : ", d)

