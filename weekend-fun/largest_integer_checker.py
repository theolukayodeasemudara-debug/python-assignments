# Ask user for three integers a, b, c
# Assume a is the largest
# If b is greater than largest, update largest
# If c is greater than largest, update largest
# Print the largest number

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

print("Largest number is:", largest)
