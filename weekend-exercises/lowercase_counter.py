# count how many lower-case letters are in a string

string = input("enter a string: ")
counter_lowercase = 0

for char in string:
    if char.islower():
        counter_lowercase += 1

print(counter_lowercase)

    
