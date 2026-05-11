# Find the sum of all even digits in a number.

num = int(input("enter a given number: "))

sum_even = 0
for index in range(1, num + 1, 2):
        sum_even += index

print(f"Total sum of even numbers: {sum_even}")
