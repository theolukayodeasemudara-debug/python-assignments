# print the divisors of a given number

input = int(input("enter a given number: "))

for index in range(1, input + 1):
    if input % index == 0:
        print(index)
