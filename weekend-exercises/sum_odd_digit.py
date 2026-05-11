# Find the sum of all odd digits in a number.

num = int(input("enter a given number: "))

sum_odd = 0
for index in range(1, num + 1, 2):
    # if index % 2 == 0:
        sum_odd += index

print(f"Total sum of even numbers: {sum_odd}")
